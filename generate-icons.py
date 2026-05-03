"""Generate icon-192.png and icon-512.png for SSD PWA."""
import struct, zlib

def make_png(size, bg=(10, 10, 10), fg=(200, 169, 110)):
    """Draw a simple SSD icon: dark background, gold wax-seal circle."""
    cx = cy = size // 2
    r_outer = int(size * 0.42)
    r_inner = int(size * 0.30)
    notch = int(size * 0.08)

    rows = []
    for y in range(size):
        row = []
        for x in range(size):
            dx, dy = x - cx, y - cy
            d = (dx*dx + dy*dy) ** 0.5
            if d <= r_outer and d >= r_inner:
                row += list(fg)
            elif d < r_inner:
                # Draw "SSD" label area — just a lighter fill
                row += [min(255, fg[0]+30), min(255, fg[1]+20), min(255, fg[2]+10)]
            else:
                row += list(bg)
        rows.append(bytes([0]) + bytes(row))  # filter byte 0 = None

    raw = b''.join(rows)
    compressed = zlib.compress(raw, 9)

    def chunk(name, data):
        c = name + data
        return struct.pack('>I', len(data)) + c + struct.pack('>I', zlib.crc32(c) & 0xffffffff)

    ihdr_data = struct.pack('>IIBBBBB', size, size, 8, 2, 0, 0, 0)
    png = (
        b'\x89PNG\r\n\x1a\n'
        + chunk(b'IHDR', ihdr_data)
        + chunk(b'IDAT', compressed)
        + chunk(b'IEND', b'')
    )
    return png

for size, name in [(192, 'icon-192.png'), (512, 'icon-512.png')]:
    with open(name, 'wb') as f:
        f.write(make_png(size))
    print(f'Created {name} ({size}x{size})')

# Minimal favicon.ico (16x16 monochrome)
with open('favicon.ico', 'wb') as f:
    png16 = make_png(16)
    # Write as ICO containing one PNG image
    # ICO header
    f.write(struct.pack('<HHH', 0, 1, 1))
    # Image directory entry
    f.write(struct.pack('<BBBBHHII', 0, 0, 0, 0, 1, 32, len(png16), 22))
    f.write(png16)
print('Created favicon.ico')
