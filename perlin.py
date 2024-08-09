import time
import math
import random

def lerp(a, b, t):
    return a + t * (b - a)

def fade(t):
    return t * t * t * (t * (t * 6 - 15) + 10)

def generate_perlin_noise_1d(size, scale):
    gradients = [random.uniform(-1, 1) for _ in range(size // scale + 1)]
    gradients[-1] = gradients[0]  # Ensure seamless looping
    
    noise = [0] * size
    for i in range(size):
        x = i / scale
        x0 = int(x)
        x1 = x0 + 1
        sx = fade(x - x0)
        
        n0 = gradients[x0 % len(gradients)]
        n1 = gradients[x1 % len(gradients)]
        
        noise[i] = lerp(n0, n1, sx)
        
    min_val, max_val = min(noise), max(noise)
    noise = [(n - min_val) / (max_val - min_val) for n in noise]
    return noise

def map_color(value, pulse_factor):
    brightness = int(value * pulse_factor * 255)
    return (brightness, brightness, brightness)

def update_leds(np, noise, offset, pulse_factor):
    size = len(np)
    for i in range(size):
        noise_value = noise[(i + offset) % size]
        np[i] = map_color(noise_value, pulse_factor)
    np.write()

def perlin_noise_pattern(np, update_period, noise_density):
    size = len(np)
    scale = max(1, size // noise_density)
    noise = generate_perlin_noise_1d(size, scale)
    offset = 0
    
    t = 0
    while True:
        # Calculate the pulse factor using a sine wave with added randomness
        pulse_factor = (math.sin(t) + 1) / 2 * (0.5 + random.random() * 0.5)
        update_leds(np, noise, offset, pulse_factor)
        
        # Randomly change the offset to create less predictable movement
        offset = (offset + random.randint(-1, 1)) % size
        t += 0.1 + random.uniform(-0.05, 0.05)  # Adding some randomness to the pulsing effect
        time.sleep(update_period / 1000)

# Example usage
import neopixel
from machine import Pin

# Initialize the NeoPixel ring
np = neopixel.NeoPixel(Pin(16), 35)  # Adjust the pin number and number of LEDs as necessary

# Start the pattern with a 50ms update period and noise density of 5
perlin_noise_pattern(np, 10, 5)
