import sys
import os
import time
import string

from rich.console import Console
from rich.text import Text
from rich.rule import Rule
from rich.panel import Panel
from rich.table import Table
from rich import box
from rich.progress import Progress, BarColumn, TextColumn, TimeElapsedColumn

from checkers import (
    check_xbox_username,
    check_steam_username,
    check_roblox_username,
    check_discord_username,
    check_chess_username,
    check_discord_vanity,
    check_fortnite_username,
    check_github_username,
    check_instagram_username,
    check_kahoot_username,
    check_lichess_username,
    check_minecraft_username,
    check_pastebin_username,
    check_replit_username,
    check_solo_username,
    check_soundcloud_username,
    check_speedrun_username,
    check_tiktok_username,
    check_twitter_username,
    check_youtube_username,
    check_twitch_username,
    check_reddit_username,
    check_pinterest_username,
    check_telegram_username,
    check_tumblr_username,
    check_deviantart_username,
    check_gitlab_username,
    check_medium_username,
    check_letterboxd_username,
    check_lastfm_username,
    check_bandcamp_username,
    check_dribbble_username,
    check_behance_username,
    check_wattpad_username,
    check_artstation_username,
    check_kofi_username,
    check_linktree_username,
    check_hackernews_username,
    check_imgur_username,
    check_npm_username,
    check_pypi_username,
    check_newgrounds_username,
    check_vk_username,
    check_producthunt_username,
    check_snapchat_username,
    check_crunchyroll_username,
    post_platform_discord,
)
from utils import (
    generate_random,
    generate_4l,
    generate_4c,
    generate_5n,
    generate_word,
    generate_semi,
    allowed_special,
    semi_supported,
    ask, ask_yn, ask_choice, print_banner,
    proxy_manager,
)

console = Console()

PLATFORM_CHECKERS = {
    "xbox":           check_xbox_username,
    "steam":          check_steam_username,
    "roblox":         check_roblox_username,
    "discord":        check_discord_username,
    "chess":          check_chess_username,
    "discord_vanity": check_discord_vanity,
    "fortnite":       check_fortnite_username,
    "github":         check_github_username,
    "instagram":      check_instagram_username,
    "kahoot":         check_kahoot_username,
    "lichess":        check_lichess_username,
    "minecraft":      check_minecraft_username,
    "pastebin":       check_pastebin_username,
    "replit":         check_replit_username,
    "solo":           check_solo_username,
    "soundcloud":     check_soundcloud_username,
    "speedrun":       check_speedrun_username,
    "tiktok":         check_tiktok_username,
    "twitter":        check_twitter_username,
    "youtube":        check_youtube_username,
    "twitch":         check_twitch_username,
    "reddit":         check_reddit_username,
    "pinterest":      check_pinterest_username,
    "telegram":       check_telegram_username,
    "tumblr":         check_tumblr_username,
    "deviantart":     check_deviantart_username,
    "gitlab":         check_gitlab_username,
    "medium":         check_medium_username,
    "letterboxd":     check_letterboxd_username,
    "lastfm":         check_lastfm_username,
    "bandcamp":       check_bandcamp_username,
    "dribbble":       check_dribbble_username,
    "behance":        check_behance_username,
    "wattpad":        check_wattpad_username,
    "artstation":     check_artstation_username,
    "kofi":           check_kofi_username,
    "linktree":       check_linktree_username,
    "hackernews":     check_hackernews_username,
    "imgur":          check_imgur_username,
    "npm":            check_npm_username,
    "pypi":           check_pypi_username,
    "newgrounds":     check_newgrounds_username,
    "vk":             check_vk_username,
    "producthunt":    check_producthunt_username,
    "snapchat":       check_snapchat_username,
    "crunchyroll":    check_crunchyroll_username,
}

PLATFORM_KEY_VARS = {
    "xbox":    "XBL_API_KEY",
    "steam":   "STEAM_API_KEY",
    "roblox":  "ROBLOX_COOKIE",
    "discord": "DISCORD_TOKEN",
}

PLATFORM_LABELS = {
    "xbox":           "Xbox",
    "steam":          "Steam",
    "roblox":         "Roblox",
    "discord":        "Discord",
    "chess":          "Chess.com",
    "discord_vanity": "Discord Vanity",
    "fortnite":       "Fortnite",
    "github":         "GitHub",
    "instagram":      "Instagram",
    "kahoot":         "Kahoot",
    "lichess":        "Lichess",
    "minecraft":      "Minecraft",
    "pastebin":       "Pastebin",
    "replit":         "Replit",
    "solo":           "Solo.to",
    "soundcloud":     "SoundCloud",
    "speedrun":       "Speedrun.com",
    "tiktok":         "TikTok",
    "twitter":        "X / Twitter",
    "youtube":        "YouTube",
    "twitch":         "Twitch",
    "reddit":         "Reddit",
    "pinterest":      "Pinterest",
    "telegram":       "Telegram",
    "tumblr":         "Tumblr",
    "deviantart":     "DeviantArt",
    "gitlab":         "GitLab",
    "medium":         "Medium",
    "letterboxd":     "Letterboxd",
    "lastfm":         "Last.fm",
    "bandcamp":       "Bandcamp",
    "dribbble":       "Dribbble",
    "behance":        "Behance",
    "wattpad":        "Wattpad",
    "artstation":     "ArtStation",
    "kofi":           "Ko-fi",
    "linktree":       "Linktree",
    "hackernews":     "Hacker News",
    "imgur":          "Imgur",
    "npm":            "NPM",
    "pypi":           "PyPI",
    "newgrounds":     "Newgrounds",
    "vk":             "VK",
    "producthunt":    "Product Hunt",
    "snapchat":       "Snapchat",
    "crunchyroll":    "Crunchyroll",
}

PLATFORM_COLORS = {
    "xbox":           "bright_green",
    "steam":          "bright_blue",
    "roblox":         "bright_red",
    "discord":        "light_violet",
    "chess":          "bright_yellow",
    "discord_vanity": "light_violet",
    "fortnite":       "bright_cyan",
    "github":         "white",
    "instagram":      "bright_magenta",
    "kahoot":         "bright_red",
    "lichess":        "bright_white",
    "minecraft":      "bright_green",
    "pastebin":       "bright_yellow",
    "replit":         "bright_blue",
    "solo":           "cyan",
    "soundcloud":     "bright_red",
    "speedrun":       "bright_green",
    "tiktok":         "white",
    "twitter":        "bright_cyan",
    "youtube":        "bright_red",
    "twitch":         "light_violet",
    "reddit":         "bright_red",
    "pinterest":      "bright_red",
    "telegram":       "bright_cyan",
    "tumblr":         "bright_blue",
    "deviantart":     "bright_green",
    "gitlab":         "bright_magenta",
    "medium":         "white",
    "letterboxd":     "bright_green",
    "lastfm":         "bright_red",
    "bandcamp":       "bright_cyan",
    "dribbble":       "bright_magenta",
    "behance":        "bright_blue",
    "wattpad":        "bright_red",
    "artstation":     "bright_blue",
    "kofi":           "bright_yellow",
    "linktree":       "bright_green",
    "hackernews":     "bright_red",
    "imgur":          "bright_green",
    "npm":            "bright_red",
    "pypi":           "bright_blue",
    "newgrounds":     "bright_yellow",
    "vk":             "bright_blue",
    "producthunt":    "bright_red",
    "snapchat":       "bright_yellow",
    "crunchyroll":    "bright_magenta",
}

KEY_REQUIRED_PLATFORMS = {"xbox", "discord"}

PLATFORM_ORDER = [
    "xbox", "steam", "roblox", "discord",
    "fortnite", "minecraft", "chess", "lichess", "kahoot", "speedrun",
    "crunchyroll", "newgrounds",
    "github", "gitlab", "npm", "pypi", "replit", "hackernews",
    "discord_vanity", "twitch", "youtube", "tiktok", "twitter", "instagram",
    "snapchat", "reddit", "pinterest", "telegram", "tumblr", "medium",
    "vk", "producthunt",
    "soundcloud", "bandcamp", "lastfm",
    "deviantart", "artstation", "dribbble", "behance", "wattpad",
    "kofi", "linktree", "solo", "imgur", "pastebin",
]

SCAN_MODES = [
    ("random", "random chars   – custom length & charset   e.g. xk3q"),
    ("4l",     "4 letters      – a-z only                  e.g. wxyz"),
    ("4c",     "4 mixed        – 2 letters + 2 numbers     e.g. ab12"),
    ("5n",     "5 numbers      – digits only               e.g. 48271"),
    ("words",  "word           – real English word         e.g. swift"),
    ("semi",   "semi           – 3 chars + _ or .          e.g. a.bc"),
]

WEBHOOK_VARS = {
    "xbox":    "DISCORD_WEBHOOK_URL",
    "steam":   "STEAM_WEBHOOK_URL",
    "roblox":  "ROBLOX_WEBHOOK_URL",
    "discord": "DISCORD_WEBHOOK_URL_DC",
}
WEBHOOK_LABELS = {
    "xbox":    "Discord webhook (Xbox channel)",
    "steam":   "Discord webhook (Steam channel)",
    "roblox":  "Discord webhook (Roblox channel)",
    "discord": "Discord webhook (Discord channel)",
}


HITS_FILE = "hits.txt"


def save_hit(username: str, platforms: list[str]) -> None:
    import datetime
    ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{ts}] {username}  ({', '.join(PLATFORM_LABELS[p] for p in platforms)})\n"
    with open(HITS_FILE, "a") as f:
        f.write(line)


def print_hit(username: str, platforms: list[str]) -> None:
    t = Text()
    t.append("  ★ HIT  ", style="bold bright_green on dark_green")
    t.append("  ", style="")
    t.append(username, style="bold bright_green")
    t.append(f"  ({len(username)} chars)", style="dim cyan")
    t.append("  →  ", style="dim white")
    t.append(", ".join(PLATFORM_LABELS[p] for p in platforms), style="dim bright_green")
    console.print(t)


def setup_proxy() -> None:
    console.print(Rule("[bold bright_cyan]Proxy / API Settings[/]", style="bright_cyan"))
    console.print()

    PROXY_MODES = [
        ("none",   "no proxies   - direct connection"),
        ("file",   "file         - load from a proxies.txt file"),
        ("manual", "manual       - type proxies one by one"),
    ]
    mode = ask_choice("Proxy source", PROXY_MODES, "none")

    if mode == "none":
        proxy_manager.clear()
        t = Text()
        t.append("  ✓ ", style="bold bright_green")
        t.append("Running without proxies", style="dim white")
        console.print(t)

    elif mode == "file":
        path = ask("Path to proxies file", "proxies.txt")
        count = proxy_manager.load_from_file(path)
        if count == 0:
            t = Text()
            t.append("  ✗ ", style="bold red")
            t.append(f"No proxies loaded from '{path}' — running direct", style="red")
            console.print(t)
            proxy_manager.clear()
        else:
            t = Text()
            t.append("  ✓ ", style="bold bright_green")
            t.append(f"{count} proxies loaded from '{path}'", style="dim white")
            console.print(t)
            proxy_manager.apply()

    elif mode == "manual":
        console.print(Text("  Enter proxies one per line (leave blank to finish):", style="dim white"))
        proxies: list[str] = []
        while True:
            raw = ask(f"Proxy {len(proxies)+1}", "").strip()
            if not raw:
                break
            proxies.append(raw)
        if proxies:
            proxy_manager.set_manual(proxies)
            proxy_manager.apply()
            t = Text()
            t.append("  ✓ ", style="bold bright_green")
            t.append(f"{len(proxies)} proxies set", style="dim white")
            console.print(t)
        else:
            proxy_manager.clear()
            t = Text()
            t.append("  ✓ ", style="bold bright_green")
            t.append("No proxies entered — running direct", style="dim white")
            console.print(t)

    console.print()


PLATFORM_CATEGORIES: list[tuple[str, list[str]]] = [
    ("Gaming", [
        "xbox", "steam", "roblox", "fortnite", "minecraft",
        "chess", "lichess", "kahoot", "speedrun", "crunchyroll", "newgrounds",
    ]),
    ("Social", [
        "discord", "instagram", "snapchat", "reddit", "pinterest",
        "telegram", "tumblr", "tiktok", "twitter", "youtube", "vk", "producthunt", "medium",
    ]),
    ("Streaming / Music", [
        "twitch", "soundcloud", "bandcamp", "lastfm",
    ]),
    ("Creative", [
        "deviantart", "artstation", "dribbble", "behance", "wattpad",
    ]),
    ("Developer", [
        "github", "gitlab", "npm", "pypi", "replit", "hackernews", "discord_vanity",
    ]),
    ("Creator Tools", [
        "kofi", "linktree", "solo", "imgur", "pastebin", "letterboxd",
    ]),
]


def _platform_menu() -> list[str]:
    numbered: list[str] = []
    for _, pids in PLATFORM_CATEGORIES:
        for pid in pids:
            numbered.append(pid)

    default_nums: set[int] = set()
    for i, pid in enumerate(numbered, 1):
        if pid in KEY_REQUIRED_PLATFORMS:
            if bool(os.environ.get(PLATFORM_KEY_VARS.get(pid, ""), "")):
                default_nums.add(i)
        else:
            default_nums.add(i)

    console.print(Rule("[bold bright_cyan]Platform Selection[/]", style="bright_cyan"))
    console.print()

    table = Table(
        box=box.SIMPLE,
        show_header=False,
        padding=(0, 1),
        border_style="dim",
        expand=False,
    )
    for _ in range(3):
        table.add_column(no_wrap=True)

    idx = 1
    for cat_name, pids in PLATFORM_CATEGORIES:
        cat_header = Text(f"  ── {cat_name} ──", style="bold bright_cyan")
        table.add_row(cat_header, Text(""), Text(""))
        chunk = []
        for pid in pids:
            label  = PLATFORM_LABELS[pid]
            avail  = idx in default_nums
            needs_key = pid in KEY_REQUIRED_PLATFORMS
            key_ok    = bool(os.environ.get(PLATFORM_KEY_VARS.get(pid, ""), ""))

            cell = Text()
            cell.append(f" {idx:>2}", style="bold bright_cyan")
            cell.append("  ", style="")
            cell.append(label, style="bold white" if avail else "dim white")
            if needs_key and not key_ok:
                cell.append(" [no key]", style="dim red")
            chunk.append(cell)
            idx += 1

        for r in range(0, len(chunk), 3):
            row = chunk[r:r + 3]
            while len(row) < 3:
                row.append(Text(""))
            table.add_row(*row)
        table.add_row(Text(""), Text(""), Text(""))

    console.print(table)

    default_str = "all" if len(default_nums) == len(numbered) else " ".join(str(n) for n in sorted(default_nums))

    console.print(Text(
        "  Enter numbers to select (e.g.  2 5 8),  a range (1-11),\n"
        "  a category (gaming / social / streaming / creative / dev / tools),\n"
        "  'all' to select all,  or press Enter for the default selection.",
        style="dim white",
    ))
    console.print()

    t = Text()
    t.append("[ ", style="dim white")
    t.append("? ", style="bold bright_cyan")
    t.append("] ", style="dim white")
    t.append("Select platforms", style="bold white")
    t.append(f" (Enter = default)", style="dim white")
    t.append(": ", style="dim white")
    console.print(t, end="")
    raw = input().strip().lower()

    if not raw:
        selected = set(default_nums)
    elif raw == "all":
        selected = set(range(1, len(numbered) + 1))
    elif raw == "none":
        selected = set()
    else:
        selected = set()
        cat_map = {
            "gaming": 0, "social": 1, "streaming": 2, "music": 2,
            "creative": 3, "dev": 4, "developer": 4, "tools": 5, "creator": 5,
        }
        tokens = raw.replace(",", " ").split()
        for token in tokens:
            if token in cat_map:
                cat_pids = PLATFORM_CATEGORIES[cat_map[token]][1]
                for p in cat_pids:
                    if p in numbered:
                        selected.add(numbered.index(p) + 1)
            elif "-" in token:
                parts = token.split("-", 1)
                try:
                    lo, hi = int(parts[0]), int(parts[1])
                    for n in range(lo, hi + 1):
                        if 1 <= n <= len(numbered):
                            selected.add(n)
                except ValueError:
                    pass
            else:
                try:
                    n = int(token)
                    if 1 <= n <= len(numbered):
                        selected.add(n)
                except ValueError:
                    pass

    result = [numbered[i - 1] for i in sorted(selected)]
    console.print()
    ok = Text()
    ok.append("  ✓ ", style="bold bright_green")
    ok.append(f"{len(result)} platforms selected", style="dim white")
    console.print(ok)
    return result


def scan_settings() -> tuple[str, int, str, int, list[str], bool]:
    console.print(Rule("[bold bright_cyan]Scan Settings[/]", style="bright_cyan"))
    console.print()

    platforms = _platform_menu()
    if not platforms:
        platforms = ["steam"]

    console.print()
    core_platforms = [p for p in platforms if p in ("xbox", "steam", "roblox", "discord")]
    special_ok = semi_supported(core_platforms) if core_platforms else False
    available_modes = [
        (k, d) for k, d in SCAN_MODES
        if k != "semi" or special_ok
    ]
    if not special_ok:
        t = Text()
        t.append("  [", style="dim")
        t.append("!", style="bold yellow")
        t.append("] semi mode disabled — selected platforms don't all support _ or .", style="yellow")
        console.print(t)

    mode = ask_choice("Scan mode", available_modes, "random")

    length  = 4
    charset = string.ascii_lowercase
    if mode == "random":
        raw_len = ask("Username length", "4")
        try:
            length = max(1, min(16, int(raw_len)))
        except ValueError:
            length = 4
        console.print(Text("  Character set:", style="dim white"))
        use_letters = ask_yn("Include letters (a-z)", "y")
        use_numbers = ask_yn("Include numbers (0-9)", "y")
        charset = ""
        if use_letters:
            charset += string.ascii_lowercase
        if use_numbers:
            charset += string.digits
        if not charset:
            charset = string.ascii_lowercase

    raw_count = ask("How many usernames to check", "50")
    try:
        count = max(1, int(raw_count))
    except ValueError:
        count = 50

    console.print()
    for pid in platforms:
        env_var = WEBHOOK_VARS.get(pid, "")
        label   = WEBHOOK_LABELS.get(pid, "")
        if not env_var or not label:
            continue
        t = Text()
        if os.environ.get(env_var, ""):
            t.append("  ✓ ", style="bold bright_green")
            t.append(f"{label} loaded", style="dim white")
        else:
            t.append("  ✗ ", style="dim yellow")
            t.append(f"{label} not set ", style="dim yellow")
            t.append(f"(set {env_var})", style="dim")
        console.print(t)
    console.print()

    platform_label = " + ".join(PLATFORM_LABELS[p] for p in platforms)
    console.print(Rule("[bold bright_cyan]Ready to scan[/]", style="bright_cyan"))
    summary = Text()
    summary.append("  Mode: ",        style="dim white")
    summary.append(mode,              style="bold bright_cyan")
    summary.append("    Count: ",     style="dim white")
    summary.append(str(count),        style="bold bright_cyan")
    summary.append("    Platforms: ", style="dim white")
    summary.append(str(len(platforms)), style="bold bright_cyan")
    summary.append(f" selected",      style="dim white")
    console.print(Panel(summary, border_style="bright_cyan", box=box.ROUNDED, padding=(0, 1)))
    console.print()

    go = ask_yn("Start scanning now", "y")
    return mode, length, charset, count, platforms, go


SKIP_ERRORS = {"no_key", "invalid_token", "invalid_cookie"}


def _next_username(mode: str, length: int, charset: str, special: frozenset[str]) -> str:
    if mode == "4l":
        return generate_4l()
    if mode == "4c":
        return generate_4c()
    if mode == "5n":
        return generate_5n()
    if mode == "words":
        return generate_word()
    if mode == "semi":
        return generate_semi(special)
    return generate_random(length, charset)


def run_scan(mode: str, length: int, charset: str, count: int, platforms: list[str]) -> list[str]:
    found:   list[str] = []
    checked: int       = 0
    seen:    set[str]  = set()
    core_platforms = [p for p in platforms if p in ("xbox", "steam", "roblox", "discord")]
    special = allowed_special(core_platforms) if core_platforms else frozenset()

    console.print(Rule("[bold bright_cyan]Scanning Usernames[/]", style="bright_cyan"))
    console.print()

    with Progress(
        TextColumn("  "),
        TextColumn("{task.fields[status]}"),
        TextColumn("[bold bright_cyan]{task.fields[last_user]}[/]"),
        BarColumn(bar_width=28, style="bright_cyan", complete_style="bright_green"),
        TextColumn("[dim white]{task.completed}/{task.total}[/]"),
        TextColumn("[bold bright_green]| {task.fields[found_count]} found[/]"),
        TimeElapsedColumn(),
        console=console,
        transient=False,
    ) as progress:
        task = progress.add_task(
            "scan",
            total=count,
            status="[dim]~[/]",
            last_user="",
            found_count=0,
        )
        rate_wait = 0

        while checked < count:
            if rate_wait > 0:
                time.sleep(rate_wait)
                rate_wait = 0

            username = _next_username(mode, length, charset, special)
            attempts = 0
            while username in seen and attempts < 200:
                username = _next_username(mode, length, charset, special)
                attempts += 1
            if username in seen:
                break
            seen.add(username)

            all_available = True
            had_error     = False

            for pid in list(platforms):
                checker_fn = PLATFORM_CHECKERS[pid]
                available, err = checker_fn(username)

                if err == "rate_limit":
                    rate_wait = 2.5
                    progress.update(task, status="[yellow]⏸[/]", last_user=username)
                    had_error = True
                    break
                elif err in SKIP_ERRORS:
                    label = PLATFORM_LABELS[pid]
                    var   = PLATFORM_KEY_VARS.get(pid, "")
                    console.print()
                    t = Text()
                    t.append("  [", style="dim")
                    t.append("!", style="bold yellow")
                    if err == "no_key":
                        t.append(f"] {label}: {var} not set — skipping.", style="yellow")
                    elif err == "invalid_token":
                        t.append(f"] {label}: token invalid — skipping.", style="yellow")
                    elif err == "invalid_cookie":
                        t.append(f"] {label}: .ROBLOSECURITY cookie invalid — skipping.", style="yellow")
                    console.print(t)
                    platforms = [p for p in platforms if p != pid]
                    if not platforms:
                        return found
                    had_error = True
                    break
                elif err:
                    progress.update(task, status="[red]✗[/]", last_user=username)
                    had_error = True
                    break
                elif not available:
                    all_available = False
                    break

            if had_error:
                if rate_wait == 0:
                    checked += 1
                    progress.advance(task)
                    time.sleep(0.1)
                continue

            if all_available:
                found.append(username)
                save_hit(username, platforms)
                for pid in platforms:
                    post_platform_discord(username, pid)
                progress.stop()
                print_hit(username, platforms)
                progress.start()
                progress.update(
                    task,
                    status="[bold bright_green]✓[/]",
                    last_user=username,
                    found_count=len(found),
                )
            else:
                progress.update(task, status="[dim red]✗[/]", last_user=username)

            if proxy_manager.active:
                proxy_manager.rotate()

            checked += 1
            progress.advance(task)
            time.sleep(0.05)

    return found


def show_found(found: list[str], platforms: list[str]) -> None:
    console.print()
    if not found:
        t = Text()
        t.append("  [", style="dim")
        t.append("i", style="cyan")
        t.append("] No available usernames found in this scan.", style="dim white")
        console.print(t)
        return

    platform_label = ", ".join(PLATFORM_LABELS[p] for p in platforms)
    console.print(Rule(
        f"[bold bright_green]Found {len(found)} Available[/]",
        style="bright_green",
    ))
    console.print()

    table = Table(box=box.SIMPLE, border_style="dim white", show_header=False, padding=(0, 3))
    table.add_column("Username",  style="bold bright_green")
    table.add_column("Length",    style="dim cyan")
    table.add_column("Platforms", style="dim white")
    table.add_column("Webhook",   style="dim white")

    posted_to = [PLATFORM_LABELS[p] for p in platforms if os.environ.get(WEBHOOK_VARS.get(p, ""), "")]
    wh_note = ("✓ " + ", ".join(posted_to)) if posted_to else "—"
    for u in found:
        table.add_row(
            u,
            f"{len(u)} chars",
            f"{len(platforms)} platforms",
            wh_note,
        )

    console.print(table)
    console.print()


def main() -> None:
    print_banner()
    setup_proxy()

    while True:
        mode, length, charset, count, platforms, go = scan_settings()

        if not go:
            console.print()
            t = Text()
            t.append("  [", style="dim")
            t.append("i", style="cyan")
            t.append("] Scan cancelled.", style="dim white")
            console.print(t)
            console.print()
            continue

        found = run_scan(mode, length, charset, count, platforms)
        show_found(found, platforms)

        if not ask_yn("Run another scan", "y"):
            console.print()
            t = Text()
            t.append("  [", style="dim")
            t.append("✓", style="bright_green")
            t.append("] Done. Goodbye.", style="white")
            console.print(t)
            console.print()
            sys.exit(0)

        print_banner()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        console.print()
        t = Text()
        t.append("\n  [", style="dim")
        t.append("✓", style="bright_green")
        t.append("] Interrupted. Goodbye.", style="white")
        console.print(t)
        console.print()
        sys.exit(0)
