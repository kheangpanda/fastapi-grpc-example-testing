import qrcode
from PIL import Image, ImageDraw

def draw_heart(draw, x, y, size, fill):
    """Draws a heart shape at (x, y) with the given size and fill color."""
    w = size // 2
    # Upper circles
    draw.pieslice([x, y, x + w, y + w], 0, 360, fill=fill)
    draw.pieslice([x + w, y, x + 2 * w, y + w], 0, 360, fill=fill)
    # Lower triangle
    draw.polygon([
        (x, y + w // 2),
        (x + size, y + w // 2),
        (x + w, y + size)
    ], fill=fill)

def generate_heart_qr(data, output_file, dot_size=20, heart_color=(255, 0, 0)):
    # Generate the basic QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=dot_size,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    
    # Get the QR code matrix
    matrix = qr.get_matrix()
    size = len(matrix) * dot_size
    
    # Create a transparent image
    heart_qr = Image.new("RGBA", (size, size), (255, 255, 255, 0))  # Transparent background
    draw = ImageDraw.Draw(heart_qr)
    
    # Replace squares with hearts
    for row_idx, row in enumerate(matrix):
        for col_idx, cell in enumerate(row):
            if cell:  # If it's a black square
                x = col_idx * dot_size
                y = row_idx * dot_size
                draw_heart(draw, x, y, dot_size, fill=heart_color)
    
    heart_qr.save(output_file, "PNG")
    print(f"Heart QR code with transparent background saved as {output_file}")

# Generate QR code for the wedding invitation URL
generate_heart_qr("https://wedding-invitation.pms.serey.tech", "wedding_heart_qr_transparent_2.png", dot_size=20, heart_color=(201, 164, 121))