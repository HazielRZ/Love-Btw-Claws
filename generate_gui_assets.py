#!/usr/bin/env python3
"""
Love Btw Claws - Ocean Breeze GUI Asset Generator
Generates all PNG assets for the Ren'Py visual novel GUI.
Theme: Glassmorphic panels with ocean-depth gradients.
"""

import os
import sys

try:
    from PIL import Image, ImageDraw, ImageFilter
except ImportError:
    print("Pillow not found. Installing...")
    os.system(f"{sys.executable} -m pip install Pillow")
    from PIL import Image, ImageDraw, ImageFilter

# === Base directory ===
BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "game", "gui")

# === Color Palette (R, G, B) ===
DEEP_OCEAN    = (13, 27, 42)      # #0D1B2A
OCEAN_MID     = (27, 58, 75)      # #1B3A4B
ACCENT_BLUE   = (46, 134, 171)    # #2E86AB
ACCENT_ORANGE = (255, 140, 66)    # #FF8C42
CORAL_HOVER   = (255, 107, 107)   # #FF6B6B
SOFT_SKY      = (184, 216, 232)   # #B8D8E8
WARM_THUMB    = (255, 179, 71)    # #FFB347

# === Helper Functions ===

def rgba(color, alpha):
    """Create RGBA tuple from RGB color and alpha (0-255)."""
    return color + (alpha,)

def alpha_int(fraction):
    """Convert a fraction (0.0-1.0) to alpha int (0-255)."""
    return int(round(fraction * 255))

def ensure_dir(filepath):
    """Ensure the directory for a filepath exists."""
    d = os.path.dirname(filepath)
    os.makedirs(d, exist_ok=True)

def make_rounded_rect(size, radius, fill, border_color=None, border_width=0):
    """Create a rounded rectangle image with optional border."""
    w, h = size
    # Use supersampling for smooth edges
    scale = 4
    sw, sh = w * scale, h * scale
    sr = radius * scale
    sbw = border_width * scale

    img = Image.new('RGBA', (sw, sh), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # Draw border first if needed
    if border_color and border_width > 0:
        draw.rounded_rectangle(
            [0, 0, sw - 1, sh - 1],
            radius=sr,
            fill=border_color
        )
        # Draw inner fill
        draw.rounded_rectangle(
            [sbw, sbw, sw - 1 - sbw, sh - 1 - sbw],
            radius=max(sr - sbw, 0),
            fill=fill
        )
    else:
        draw.rounded_rectangle(
            [0, 0, sw - 1, sh - 1],
            radius=sr,
            fill=fill
        )

    # Downscale for antialiasing
    img = img.resize((w, h), Image.LANCZOS)
    return img

def make_rounded_rect_gradient_h(size, radius, left_color, right_color, border_color=None, border_width=0):
    """Create a rounded rectangle with horizontal gradient fill and optional border."""
    w, h = size
    # Create gradient
    gradient = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    for x in range(w):
        t = x / max(w - 1, 1)
        r = int(left_color[0] + (right_color[0] - left_color[0]) * t)
        g = int(left_color[1] + (right_color[1] - left_color[1]) * t)
        b = int(left_color[2] + (right_color[2] - left_color[2]) * t)
        a = int(left_color[3] + (right_color[3] - left_color[3]) * t)
        for y in range(h):
            gradient.putpixel((x, y), (r, g, b, a))

    # Create mask with rounded rectangle
    scale = 4
    mask_big = Image.new('L', (w * scale, h * scale), 0)
    draw_mask = ImageDraw.Draw(mask_big)
    draw_mask.rounded_rectangle(
        [0, 0, w * scale - 1, h * scale - 1],
        radius=radius * scale,
        fill=255
    )
    mask = mask_big.resize((w, h), Image.LANCZOS)

    # Apply mask
    result = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    result.paste(gradient, (0, 0), mask)

    # Add border if needed
    if border_color and border_width > 0:
        border_img = Image.new('RGBA', (w * scale, h * scale), (0, 0, 0, 0))
        draw_border = ImageDraw.Draw(border_img)
        # Outer rounded rect
        draw_border.rounded_rectangle(
            [0, 0, w * scale - 1, h * scale - 1],
            radius=radius * scale,
            outline=border_color,
            width=border_width * scale
        )
        border_img = border_img.resize((w, h), Image.LANCZOS)
        result = Image.alpha_composite(result, border_img)

    return result

def make_rounded_rect_gradient_v(size, radius, top_color, bottom_color, border_color=None, border_width=0):
    """Create a rounded rectangle with vertical gradient fill."""
    w, h = size
    gradient = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    for y in range(h):
        t = y / max(h - 1, 1)
        r = int(top_color[0] + (bottom_color[0] - top_color[0]) * t)
        g = int(top_color[1] + (bottom_color[1] - top_color[1]) * t)
        b = int(top_color[2] + (bottom_color[2] - top_color[2]) * t)
        a = int(top_color[3] + (bottom_color[3] - top_color[3]) * t)
        for x in range(w):
            gradient.putpixel((x, y), (r, g, b, a))

    scale = 4
    mask_big = Image.new('L', (w * scale, h * scale), 0)
    draw_mask = ImageDraw.Draw(mask_big)
    draw_mask.rounded_rectangle(
        [0, 0, w * scale - 1, h * scale - 1],
        radius=radius * scale,
        fill=255
    )
    mask = mask_big.resize((w, h), Image.LANCZOS)

    result = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    result.paste(gradient, (0, 0), mask)

    if border_color and border_width > 0:
        border_img = Image.new('RGBA', (w * scale, h * scale), (0, 0, 0, 0))
        draw_border = ImageDraw.Draw(border_img)
        draw_border.rounded_rectangle(
            [0, 0, w * scale - 1, h * scale - 1],
            radius=radius * scale,
            outline=border_color,
            width=border_width * scale
        )
        border_img = border_img.resize((w, h), Image.LANCZOS)
        result = Image.alpha_composite(result, border_img)

    return result

def make_circle(size, fill, border_color=None, border_width=0):
    """Create a circle image."""
    w, h = size
    scale = 4
    img = Image.new('RGBA', (w * scale, h * scale), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    if border_color and border_width > 0:
        draw.ellipse([0, 0, w * scale - 1, h * scale - 1], fill=border_color)
        bw = border_width * scale
        draw.ellipse([bw, bw, w * scale - 1 - bw, h * scale - 1 - bw], fill=fill)
    else:
        draw.ellipse([0, 0, w * scale - 1, h * scale - 1], fill=fill)
    img = img.resize((w, h), Image.LANCZOS)
    return img

def save_png(img, rel_path):
    """Save an image to the gui directory."""
    full_path = os.path.join(BASE_DIR, rel_path)
    ensure_dir(full_path)
    img.save(full_path, 'PNG')
    print(f"  [OK] {rel_path} ({img.size[0]}x{img.size[1]})")
    return full_path

# === Asset Generation Functions ===

def gen_textbox():
    """1. gui/textbox.png (1920 x 278)"""
    w, h = 1920, 278
    img = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    # Gradient: transparent top → semi-transparent dark bottom
    for y in range(h):
        t = y / (h - 1)
        # Ease-in curve for a more natural fade
        t = t * t
        alpha = int(t * 0.70 * 255)
        r, g, b = DEEP_OCEAN
        for x in range(w):
            img.putpixel((x, y), (r, g, b, alpha))
    # Thin accent line at the top (2px)
    draw = ImageDraw.Draw(img)
    line_color = rgba(ACCENT_BLUE, alpha_int(0.60))
    draw.rectangle([0, 0, w - 1, 1], fill=line_color)
    save_png(img, "textbox.png")

def gen_namebox():
    """2. gui/namebox.png (360 x 57)"""
    w, h = 360, 57
    fill = rgba(DEEP_OCEAN, alpha_int(0.85))
    border = rgba(ACCENT_ORANGE, alpha_int(0.70))
    # Create the pill shape
    img = make_rounded_rect((w, h), 15, fill)
    # Add bottom border line (2px)
    scale = 4
    border_layer = Image.new('RGBA', (w * scale, h * scale), (0, 0, 0, 0))
    draw = ImageDraw.Draw(border_layer)
    # Draw 2px line at bottom inside the rounded rect
    draw.rounded_rectangle(
        [0, 0, w * scale - 1, h * scale - 1],
        radius=15 * scale,
        outline=border,
        width=2 * scale
    )
    border_layer = border_layer.resize((w, h), Image.LANCZOS)
    # We only want the bottom border - mask out the top part
    # Actually, let's just overlay the full border but make it subtle
    # For a bottom-only effect, we'll create a mask
    mask = Image.new('L', (w, h), 0)
    draw_mask = ImageDraw.Draw(mask)
    draw_mask.rectangle([0, h - 10, w, h], fill=255)
    border_final = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    border_final.paste(border_layer, (0, 0), mask)
    img = Image.alpha_composite(img, border_final)
    save_png(img, "namebox.png")

def gen_frame():
    """3. gui/frame.png (600 x 400)"""
    w, h = 600, 400
    fill = rgba(DEEP_OCEAN, alpha_int(0.85))
    border = rgba(ACCENT_BLUE, alpha_int(0.40))
    img = make_rounded_rect((w, h), 10, fill, border, 1)
    save_png(img, "frame.png")

def gen_overlay_main_menu():
    """4. gui/overlay/main_menu.png (1920 x 1080)"""
    w, h = 1920, 1080
    img = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    r, g, b = DEEP_OCEAN
    # Left 35% solid at 90% opacity, fade to transparent by 50%
    fade_start = int(w * 0.35)
    fade_end = int(w * 0.50)
    accent_x = int(w * 0.33)

    for x in range(w):
        if x < fade_start:
            alpha = alpha_int(0.90)
        elif x < fade_end:
            t = (x - fade_start) / (fade_end - fade_start)
            alpha = int(alpha_int(0.90) * (1 - t))
        else:
            alpha = 0
        col = (r, g, b, alpha)
        for y in range(h):
            img.putpixel((x, y), col)

    # Vertical accent line at ~33%
    draw = ImageDraw.Draw(img)
    line_color = rgba(ACCENT_BLUE, alpha_int(0.50))
    draw.rectangle([accent_x, 0, accent_x + 1, h - 1], fill=line_color)
    save_png(img, os.path.join("overlay", "main_menu.png"))

def gen_overlay_game_menu():
    """5. gui/overlay/game_menu.png (1920 x 1080)"""
    w, h = 1920, 1080
    img = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    r, g, b = DEEP_OCEAN

    # Base at 85% opacity
    base_alpha = alpha_int(0.85)
    # Left 420px slightly lighter
    nav_r, nav_g, nav_b = OCEAN_MID

    for x in range(w):
        if x < 420:
            col = (nav_r, nav_g, nav_b, base_alpha)
        else:
            col = (r, g, b, base_alpha)
        for y in range(h):
            img.putpixel((x, y), col)

    # Accent line at x=420
    draw = ImageDraw.Draw(img)
    line_color = rgba(ACCENT_BLUE, alpha_int(0.60))
    draw.rectangle([420, 140, 421, 980], fill=line_color)
    save_png(img, os.path.join("overlay", "game_menu.png"))

def gen_overlay_confirm():
    """6. gui/overlay/confirm.png (1920 x 1080)"""
    w, h = 1920, 1080
    fill = rgba(DEEP_OCEAN, alpha_int(0.75))
    img = Image.new('RGBA', (w, h), fill)
    save_png(img, os.path.join("overlay", "confirm.png"))

def gen_notify():
    """7. gui/notify.png (600 x 50)"""
    w, h = 600, 50
    fill = rgba(DEEP_OCEAN, alpha_int(0.85))
    border = rgba(ACCENT_BLUE, alpha_int(0.30))
    img = make_rounded_rect((w, h), 12, fill, border, 1)
    save_png(img, "notify.png")

def gen_skip():
    """8. gui/skip.png (300 x 40)"""
    w, h = 300, 40
    fill = rgba(DEEP_OCEAN, alpha_int(0.80))
    img = make_rounded_rect((w, h), 10, fill)
    save_png(img, "skip.png")

def gen_nvl():
    """9. gui/nvl.png (1920 x 1080)"""
    w, h = 1920, 1080
    fill = rgba(DEEP_OCEAN, alpha_int(0.80))
    img = Image.new('RGBA', (w, h), fill)
    save_png(img, "nvl.png")

def gen_button_idle():
    """10. gui/button/idle_background.png (600 x 50)"""
    w, h = 600, 50
    fill = rgba(OCEAN_MID, alpha_int(0.15))
    img = make_rounded_rect((w, h), 8, fill)
    save_png(img, os.path.join("button", "idle_background.png"))

def gen_button_hover():
    """11. gui/button/hover_background.png (600 x 50)"""
    w, h = 600, 50
    left = rgba(ACCENT_BLUE, alpha_int(0.25))
    right = rgba(ACCENT_ORANGE, alpha_int(0.15))
    img = make_rounded_rect_gradient_h((w, h), 8, left, right)
    save_png(img, os.path.join("button", "hover_background.png"))

def gen_choice_idle():
    """12. gui/button/choice_idle_background.png (1185 x 60)"""
    w, h = 1185, 60
    fill = rgba(DEEP_OCEAN, alpha_int(0.75))
    border = rgba(ACCENT_BLUE, alpha_int(0.35))
    img = make_rounded_rect((w, h), 30, fill, border, 1)
    save_png(img, os.path.join("button", "choice_idle_background.png"))

def gen_choice_hover():
    """13. gui/button/choice_hover_background.png (1185 x 60)"""
    w, h = 1185, 60
    left = rgba(ACCENT_BLUE, alpha_int(0.50))
    right = rgba(ACCENT_ORANGE, alpha_int(0.40))
    border = rgba(ACCENT_ORANGE, alpha_int(0.50))
    img = make_rounded_rect_gradient_h((w, h), 30, left, right, border, 2)
    save_png(img, os.path.join("button", "choice_hover_background.png"))

def gen_slot_idle():
    """14. gui/button/slot_idle_background.png (414 x 309)"""
    w, h = 414, 309
    fill = rgba(DEEP_OCEAN, alpha_int(0.80))
    border = rgba(ACCENT_BLUE, alpha_int(0.30))
    img = make_rounded_rect((w, h), 12, fill, border, 1)
    save_png(img, os.path.join("button", "slot_idle_background.png"))

def gen_slot_hover():
    """15. gui/button/slot_hover_background.png (414 x 309)"""
    w, h = 414, 309
    fill = rgba(OCEAN_MID, alpha_int(0.85))
    border = rgba(ACCENT_ORANGE, alpha_int(0.50))
    img = make_rounded_rect((w, h), 12, fill, border, 2)
    save_png(img, os.path.join("button", "slot_hover_background.png"))

def gen_quick_idle():
    """16. gui/button/quick_idle_background.png (200 x 36)"""
    w, h = 200, 36
    fill = rgba(OCEAN_MID, alpha_int(0.10))
    img = make_rounded_rect((w, h), 6, fill)
    save_png(img, os.path.join("button", "quick_idle_background.png"))

def gen_quick_hover():
    """17. gui/button/quick_hover_background.png (200 x 36)"""
    w, h = 200, 36
    fill = rgba(ACCENT_BLUE, alpha_int(0.20))
    img = make_rounded_rect((w, h), 6, fill)
    save_png(img, os.path.join("button", "quick_hover_background.png"))

def gen_slider_h_idle_bar():
    """18. gui/slider/horizontal_idle_bar.png (1920 x 38)"""
    w, h = 1920, 38
    fill = rgba(OCEAN_MID, alpha_int(0.80))
    border = rgba(ACCENT_BLUE, alpha_int(0.25))
    img = make_rounded_rect((w, h), 19, fill, border, 1)
    save_png(img, os.path.join("slider", "horizontal_idle_bar.png"))

def gen_slider_h_hover_bar():
    """19. gui/slider/horizontal_hover_bar.png (1920 x 38)"""
    w, h = 1920, 38
    left = rgba(ACCENT_BLUE, alpha_int(0.40))
    right = rgba(ACCENT_ORANGE, alpha_int(0.30))
    border = rgba(ACCENT_BLUE, alpha_int(0.40))
    img = make_rounded_rect_gradient_h((w, h), 19, left, right, border, 1)
    save_png(img, os.path.join("slider", "horizontal_hover_bar.png"))

def gen_slider_h_idle_thumb():
    """20. gui/slider/horizontal_idle_thumb.png (38 x 38)"""
    s = 38
    fill = rgba(SOFT_SKY, alpha_int(0.90))
    border = rgba(ACCENT_BLUE, alpha_int(0.80))
    img = make_circle((s, s), fill, border, 2)
    save_png(img, os.path.join("slider", "horizontal_idle_thumb.png"))

def gen_slider_h_hover_thumb():
    """21. gui/slider/horizontal_hover_thumb.png (38 x 38)"""
    s = 38
    fill = rgba(ACCENT_ORANGE, alpha_int(0.95))
    border = rgba(WARM_THUMB, alpha_int(0.80))
    img = make_circle((s, s), fill, border, 2)
    # Add subtle glow
    glow = Image.new('RGBA', (s + 8, s + 8), (0, 0, 0, 0))
    glow_draw = ImageDraw.Draw(glow)
    glow_draw.ellipse([0, 0, s + 7, s + 7], fill=rgba(ACCENT_ORANGE, 30))
    glow = glow.filter(ImageFilter.GaussianBlur(2))
    result = Image.new('RGBA', (s, s), (0, 0, 0, 0))
    result.paste(glow, (-4, -4))
    result = Image.alpha_composite(result, img)
    save_png(result, os.path.join("slider", "horizontal_hover_thumb.png"))

def gen_scrollbar_h_idle_bar():
    """22. gui/scrollbar/horizontal_idle_bar.png (1920 x 18)"""
    w, h = 1920, 18
    fill = rgba(OCEAN_MID, alpha_int(0.50))
    img = make_rounded_rect((w, h), h // 2, fill)
    save_png(img, os.path.join("scrollbar", "horizontal_idle_bar.png"))

def gen_scrollbar_h_hover_bar():
    """23. gui/scrollbar/horizontal_hover_bar.png (1920 x 18)"""
    w, h = 1920, 18
    fill = rgba(ACCENT_BLUE, alpha_int(0.50))
    img = make_rounded_rect((w, h), h // 2, fill)
    save_png(img, os.path.join("scrollbar", "horizontal_hover_bar.png"))

def gen_scrollbar_h_idle_thumb():
    """24. gui/scrollbar/horizontal_idle_thumb.png (200 x 18)"""
    w, h = 200, 18
    fill = rgba(SOFT_SKY, alpha_int(0.60))
    img = make_rounded_rect((w, h), h // 2, fill)
    save_png(img, os.path.join("scrollbar", "horizontal_idle_thumb.png"))

def gen_scrollbar_h_hover_thumb():
    """25. gui/scrollbar/horizontal_hover_thumb.png (200 x 18)"""
    w, h = 200, 18
    fill = rgba(ACCENT_ORANGE, alpha_int(0.70))
    img = make_rounded_rect((w, h), h // 2, fill)
    save_png(img, os.path.join("scrollbar", "horizontal_hover_thumb.png"))

def gen_scrollbar_v_idle_bar():
    """26. gui/scrollbar/vertical_idle_bar.png (18 x 1080)"""
    w, h = 18, 1080
    fill = rgba(OCEAN_MID, alpha_int(0.50))
    img = make_rounded_rect((w, h), w // 2, fill)
    save_png(img, os.path.join("scrollbar", "vertical_idle_bar.png"))

def gen_scrollbar_v_hover_bar():
    """27. gui/scrollbar/vertical_hover_bar.png (18 x 1080)"""
    w, h = 18, 1080
    fill = rgba(ACCENT_BLUE, alpha_int(0.50))
    img = make_rounded_rect((w, h), w // 2, fill)
    save_png(img, os.path.join("scrollbar", "vertical_hover_bar.png"))

def gen_scrollbar_v_idle_thumb():
    """28. gui/scrollbar/vertical_idle_thumb.png (18 x 200)"""
    w, h = 18, 200
    fill = rgba(SOFT_SKY, alpha_int(0.60))
    img = make_rounded_rect((w, h), w // 2, fill)
    save_png(img, os.path.join("scrollbar", "vertical_idle_thumb.png"))

def gen_scrollbar_v_hover_thumb():
    """29. gui/scrollbar/vertical_hover_thumb.png (18 x 200)"""
    w, h = 18, 200
    fill = rgba(ACCENT_ORANGE, alpha_int(0.70))
    img = make_rounded_rect((w, h), w // 2, fill)
    save_png(img, os.path.join("scrollbar", "vertical_hover_thumb.png"))

def gen_bar_left():
    """30. gui/bar/left.png (1920 x 38)"""
    w, h = 1920, 38
    left = rgba(ACCENT_BLUE, alpha_int(0.90))
    right = rgba(ACCENT_ORANGE, alpha_int(0.80))
    # Use rounded left end only - we'll create full rounded then crop conceptually
    # Actually for Ren'Py bars, we want fully rounded pill, the engine handles clipping
    img = make_rounded_rect_gradient_h((w, h), 19, left, right)
    save_png(img, os.path.join("bar", "left.png"))

def gen_bar_right():
    """31. gui/bar/right.png (1920 x 38)"""
    w, h = 1920, 38
    fill = rgba(OCEAN_MID, alpha_int(0.60))
    img = make_rounded_rect((w, h), 19, fill)
    save_png(img, os.path.join("bar", "right.png"))

def gen_bar_top():
    """32. gui/bar/top.png (38 x 1080)"""
    w, h = 38, 1080
    top = rgba(ACCENT_BLUE, alpha_int(0.90))
    bottom = rgba(ACCENT_ORANGE, alpha_int(0.80))
    img = make_rounded_rect_gradient_v((w, h), 19, top, bottom)
    save_png(img, os.path.join("bar", "top.png"))

def gen_bar_bottom():
    """33. gui/bar/bottom.png (38 x 1080)"""
    w, h = 38, 1080
    fill = rgba(OCEAN_MID, alpha_int(0.60))
    img = make_rounded_rect((w, h), 19, fill)
    save_png(img, os.path.join("bar", "bottom.png"))


# === Optimized overlay generators using column-based approach ===

def gen_textbox_fast():
    """1. gui/textbox.png (1920 x 278) - optimized"""
    w, h = 1920, 278
    img = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    pixels = img.load()
    r, g, b = DEEP_OCEAN
    for y in range(h):
        t = y / (h - 1)
        t2 = t * t  # ease-in
        alpha = int(t2 * 0.70 * 255)
        col = (r, g, b, alpha)
        for x in range(w):
            pixels[x, y] = col
    # Accent line
    line_color = rgba(ACCENT_BLUE, alpha_int(0.60))
    for x in range(w):
        pixels[x, 0] = line_color
        pixels[x, 1] = line_color
    save_png(img, "textbox.png")

def gen_overlay_main_menu_fast():
    """4. gui/overlay/main_menu.png (1920 x 1080) - optimized"""
    w, h = 1920, 1080
    img = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    pixels = img.load()
    r, g, b = DEEP_OCEAN
    fade_start = int(w * 0.35)
    fade_end = int(w * 0.50)
    accent_x = int(w * 0.33)
    max_alpha = alpha_int(0.90)
    line_color = rgba(ACCENT_BLUE, alpha_int(0.50))

    for x in range(w):
        if x < fade_start:
            alpha = max_alpha
        elif x < fade_end:
            t = (x - fade_start) / (fade_end - fade_start)
            alpha = int(max_alpha * (1 - t))
        else:
            alpha = 0
        col = (r, g, b, alpha)
        if x == accent_x or x == accent_x + 1:
            col_with_line = line_color
        else:
            col_with_line = None
        for y in range(h):
            if col_with_line:
                # Blend accent line over base
                pixels[x, y] = col_with_line
            else:
                pixels[x, y] = col
    save_png(img, os.path.join("overlay", "main_menu.png"))

def gen_overlay_game_menu_fast():
    """5. gui/overlay/game_menu.png (1920 x 1080) - optimized"""
    w, h = 1920, 1080
    img = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    pixels = img.load()
    base_alpha = alpha_int(0.85)
    r, g, b = DEEP_OCEAN
    nr, ng, nb = OCEAN_MID
    line_color = rgba(ACCENT_BLUE, alpha_int(0.60))

    for x in range(w):
        if x < 420:
            col = (nr, ng, nb, base_alpha)
        else:
            col = (r, g, b, base_alpha)
        is_line = (x == 420 or x == 421)
        for y in range(h):
            if is_line and 140 <= y <= 980:
                pixels[x, y] = line_color
            else:
                pixels[x, y] = col
    save_png(img, os.path.join("overlay", "game_menu.png"))


# === Main ===

def main():
    print("=" * 60)
    print("Love Btw Claws - Ocean Breeze GUI Asset Generator")
    print("=" * 60)
    print(f"Output directory: {BASE_DIR}")
    print()

    generators = [
        ("1/33 Textbox", gen_textbox_fast),
        ("2/33 Namebox", gen_namebox),
        ("3/33 Frame", gen_frame),
        ("4/33 Overlay: Main Menu", gen_overlay_main_menu_fast),
        ("5/33 Overlay: Game Menu", gen_overlay_game_menu_fast),
        ("6/33 Overlay: Confirm", gen_overlay_confirm),
        ("7/33 Notify", gen_notify),
        ("8/33 Skip", gen_skip),
        ("9/33 NVL", gen_nvl),
        ("10/33 Button: Idle", gen_button_idle),
        ("11/33 Button: Hover", gen_button_hover),
        ("12/33 Choice: Idle", gen_choice_idle),
        ("13/33 Choice: Hover", gen_choice_hover),
        ("14/33 Slot: Idle", gen_slot_idle),
        ("15/33 Slot: Hover", gen_slot_hover),
        ("16/33 Quick: Idle", gen_quick_idle),
        ("17/33 Quick: Hover", gen_quick_hover),
        ("18/33 Slider H Idle Bar", gen_slider_h_idle_bar),
        ("19/33 Slider H Hover Bar", gen_slider_h_hover_bar),
        ("20/33 Slider H Idle Thumb", gen_slider_h_idle_thumb),
        ("21/33 Slider H Hover Thumb", gen_slider_h_hover_thumb),
        ("22/33 Scrollbar H Idle Bar", gen_scrollbar_h_idle_bar),
        ("23/33 Scrollbar H Hover Bar", gen_scrollbar_h_hover_bar),
        ("24/33 Scrollbar H Idle Thumb", gen_scrollbar_h_idle_thumb),
        ("25/33 Scrollbar H Hover Thumb", gen_scrollbar_h_hover_thumb),
        ("26/33 Scrollbar V Idle Bar", gen_scrollbar_v_idle_bar),
        ("27/33 Scrollbar V Hover Bar", gen_scrollbar_v_hover_bar),
        ("28/33 Scrollbar V Idle Thumb", gen_scrollbar_v_idle_thumb),
        ("29/33 Scrollbar V Hover Thumb", gen_scrollbar_v_hover_thumb),
        ("30/33 Bar: Left", gen_bar_left),
        ("31/33 Bar: Right", gen_bar_right),
        ("32/33 Bar: Top", gen_bar_top),
        ("33/33 Bar: Bottom", gen_bar_bottom),
    ]

    success = 0
    failed = 0
    for label, func in generators:
        try:
            print(f"\nGenerating {label}...")
            func()
            success += 1
        except Exception as e:
            print(f"  [FAIL] {label}: {e}")
            failed += 1

    print()
    print("=" * 60)
    print(f"Done! {success} succeeded, {failed} failed out of {len(generators)} assets.")
    print("=" * 60)

if __name__ == "__main__":
    main()
