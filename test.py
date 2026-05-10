import requests
from bs4 import BeautifulSoup


def print_google_doc_grid(url: str) -> None:
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    cells = [cell.get_text(strip=True) for cell in soup.find_all("td")]

    points = []

    # Data appears as repeating triples:
    # x-coordinate, character, y-coordinate
    for i in range(0, len(cells), 3):
        try:
            x = int(cells[i])
            char = cells[i + 1]
            y = int(cells[i + 2])
            points.append((x, y, char))
        except (ValueError, IndexError):
            continue

    if not points:
        return

    max_x = max(x for x, y, char in points)
    max_y = max(y for x, y, char in points)

    grid = [[" " for _ in range(max_x + 1)] for _ in range(max_y + 1)]

    for x, y, char in points:
        grid[y][x] = " " if char == "░" else char

    for y in range(max_y, -1, -1):
        print("".join(grid[y]))


print_google_doc_grid("https://docs.google.com/document/d/e/2PACX-1vSvM5gDlNvt7npYHhp_XfsJvuntUhq184By5xO_pA4b_gCWeXb6dM6ZxwN8rE6S4ghUsCj2VKR21oEP/pub")