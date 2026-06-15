#!/usr/bin/env python3
class WZMLStyle:
    # ===== START MESSAGE =====
    ST_BN1_NAME = '☀️ OWNER ☀️'
    ST_BN1_URL = 'https://t.me/leonaardos'
    ST_BN2_NAME = '🚀 Updates 🚀'
    ST_BN2_URL = 'https://t.me/leonaardos'
    ST_MSG = '''╔════════════════════════════════╗
║  🚀 𝐖𝐙𝐌𝐋-𝐗 𝐌𝐨𝐝𝐞𝐫𝐧 𝐓𝐡𝐞𝐦𝐞 🚀  ║
╚════════════════════════════════╝

<b>✨ Welcome to Mirror-Leech Bot!</b>

This bot can mirror all your links, files, and torrents to:
  • 🌐 Google Drive
  • ☁️ RClone Cloud Storage
  • 📱 Telegram
  • ⚡ DDL Servers

<b>📚 Available Commands:</b>
Type {help_command} to see all commands

<b>🔐 Source:</b> WZML-X Modified with Custom Enhancements ❤️'''
    
    ST_BOTPM = '''╔════════════════════════════════╗
║  📥 Bot PM Mode Activated 📥   ║
╚════════════════════════════════╝

<b>✅ Success!</b> All files and links will now be sent here.

Start using the bot at: <b><u>@YourBotUsername</u></b>

📌 <i>Your files will appear below...</i>'''
    
    ST_UNAUTH = '''╔════════════════════════════════╗
║  ❌ Unauthorized Access ❌      ║
╚════════════════════════════════╝

<b>⚠️ You are not authorized to use this bot!</b>

🔧 <b>Solution:</b> Deploy your own WZML-X Mirror-Leech bot

📖 <a href="https://github.com/weebzone/WZML-X">Official Repository</a>'''
    
    OWN_TOKEN_GENERATE = '''<b>🔴 Invalid Token!</b>

This temporary token doesn\'t belong to you.
Please generate your own token.'''
    
    USED_TOKEN = '''<b>🔴 Token Already Used!</b>

This token has already been activated.
Please generate a new one.'''
    
    LOGGED_PASSWORD = '''<b>✅ Already Logged In</b>

Bot is already logged in via password.
No need to use temporary tokens.'''
    
    ACTIVATE_BUTTON = '🔓 Activate Temporary Token'
    TOKEN_MSG = '''╔════════════════════════════════╗
║  🎟️  Generated Token 🎟️        ║
╚════════════════════════════════╝

<b>🔑 Temporary Token:</b>
<code>{token}</code>

⏰ <b>Validity:</b> {validity}
⚡ <b>Status:</b> Active & Ready to Use'''
    
    # ===== LOGIN MESSAGES =====
    ACTIVATED = '✅ Token Activated Successfully ✅'
    LOGGED_IN = '<b>✅ Bot Already Logged In</b>\n\nYou\'re already authenticated.'
    INVALID_PASS = '<b>❌ Invalid Password!</b>\n\nPlease enter the correct password.'
    PASS_LOGGED = '<b>✅ Permanent Login Successful!</b>\n\nYou can now access all features.'
    LOGIN_USED = '<b>📌 Login Command Usage:</b>\n\n<code>/cmd [password]</code>'
    
    # ===== HELP MENU =====
    LOG_DISPLAY_BT = '📑 Log Display'
    WEB_PASTE_BT = '📨 Web Paste'
    BASIC_BT = 'ℹ️ Basic'
    USER_BT = '👤 Users'
    MICS_BT = '🔧 Misc'
    O_S_BT = '👑 Owner/Sudo'
    CLOSE_BT = '✖️ Close'
    HELP_HEADER = '''╔════════════════════════════════╗
║  📚 Help Guide Menu 📚         ║
╚════════════════════════════════╝

<b>💡 Tip:</b> Click on any command to see detailed information.'''
    
    # ===== STATISTICS =====
    ENG_INFO = '''╔════════════════════════════════╗
║  🚀 Engine Information 🚀       ║
╚════════════════════════════════╝

<b>🐍 Main Dependencies:</b>
  ├─ Python: {pyt}
  ├─ Pyrogram: {pgram}
  └─ TgCrypto: {tgcr}

<b>❄️ Download Engines:</b>
  ├─ Aria2: {ar}
  ├─ qBittorrent: {qb}
  ├─ YT-DLP: {yt}
  └─ FFmpeg: {ff}

<b>☁️ Cloud & Storage:</b>
  ├─ Mega SDK: {me}
  ├─ RClone: {rcl}
  ├─ 7z: {zz}
  └─ Google-API: Included

<a href="https://t.me/leonaardos">👨‍💻 Bot by leo♌</a>'''
    
    BOT_STATS = '''╔════════════════════════════════╗
║  📊 Bot Statistics 📊           ║
╚════════════════════════════════╝

<b>⏱️ Bot Uptime:</b> {bot_uptime}

<b>🔴 RAM (Memory):</b>
  │ {ram_bar} {ram}%
  ├─ Used: {ram_u}
  ├─ Free: {ram_f}
  └─ Total: {ram_t}

<b>⚙️ Swap Memory:</b>
  │ {swap_bar} {swap}%
  ├─ Used: {swap_u}
  ├─ Free: {swap_f}
  └─ Total: {swap_t}

<b>💿 Disk Storage:</b>
  │ {disk_bar} {disk}%
  ├─ Read: {disk_read}
  ├─ Write: {disk_write}
  ├─ Used: {disk_u}
  ├─ Free: {disk_f}
  └─ Total: {disk_t}

<a href="https://t.me/leonaardos">👨‍💻 Bot by leo♌</a>'''
    
    SYS_STATS = '''╔════════════════════════════════╗
║  🖥️  System Statistics 🖥️      ║
╚════════════════════════════════╝

<b>📅 OS Information:</b>
  ├─ Uptime: {os_uptime}
  ├─ Version: {os_version}
  └─ Architecture: {os_arch}

<b>🛜 Network Stats:</b>
  ├─ Upload: {up_data}
  ├─ Download: {dl_data}
  ├─ Packets Sent: {pkt_sent}k
  ├─ Packets Recv: {pkt_recv}k
  └─ Total I/O: {tl_data}

<b>🖥️ CPU Performance:</b>
  │ {cpu_bar} {cpu}%
  ├─ Frequency: {cpu_freq}
  ├─ System Load: {sys_load}
  ├─ Physical Cores: {p_core}
  ├─ Virtual Cores: {v_core}
  ├─ Total Cores: {total_core}
  └─ Usable: {cpu_use}

<a href="https://t.me/leonaardos">👨‍💻 Bot by leo♌</a>'''
    
    REPO_STATS = '''╔════════════════════════════════╗
║  📦 Repository Statistics 📦   ║
╚════════════════════════════════╝

<b>📝 Version Information:</b>
  ├─ Last Updated: {last_commit}
  ├─ Current Version: {bot_version}
  ├─ Latest Version: {lat_version}
  └─ Last ChangeLog: {commit_details}

<b>💭 Status:</b> <code>{remarks}</code>

<a href="https://t.me/leonaardos">👨‍💻 Bot by leo♌</a>'''
    
    BOT_LIMITS = '''╔════════════════════════════════╗
║  ⚙️  Bot Limitations ⚙️         ║
╚════════════════════════════════╝

<b>📥 Download Limits:</b>
  ├─ Direct Links: {DL} GB
  ├─ Torrents: {TL} GB
  ├─ Google Drive: {GL} GB
  ├─ YouTube (YT-DLP): {YL} GB
  ├─ Playlists: {PL}
  ├─ Mega: {ML} GB
  ├─ Clone: {CL} GB
  └─ Leech: {LL} GB

<b>🔐 Security & Limits:</b>
  ├─ Token Validity: {TV}
  ├─ User Time Limit: {UTI} / task
  ├─ User Parallel Tasks: {UT}
  └─ Bot Parallel Tasks: {BT}

<a href="https://t.me/leonaardos">👨‍💻 Bot by leo♌</a>'''
    
    # ===== RESTARTING =====
    RESTARTING = '<i>🔄 Restarting bot... Please wait...</i>'
    RESTART_SUCCESS = '''╔════════════════════════════════╗
║  ✅ Bot Restarted Successfully ║
╚════════════════════════════════╝

📅 <b>Date:</b> {date}
⏰ <b>Time:</b> {time}
🌍 <b>TimeZone:</b> {timz}
📦 <b>Version:</b> {version}'''
    
    RESTARTED = '''<b>✅ Bot Restarted!</b>

All systems are back online.'''
    
    # ===== PING =====
    PING = '<i>🔍 Starting Ping...</i>'
    PING_VALUE = '<b>🏓 Pong!</b>\n<code>{value} ms</code>'
    
    # ===== DOWNLOAD START =====
    LINKS_START = """<b>🚀 Task Started!</b>
  ├─ Mode: {Mode}
  └─ By: {Tag}

"""
    LINKS_SOURCE = """<b>📎 Source Information:</b>
  └─ Added On: {On}
─────────────────────────────────
{Source}
─────────────────────────────────

"""
    
    # ===== UPLOAD COMPLETE =====
    PM_START = "➜ <b>Task Started</b>\n├─ Link: <a href='{msg_link}'>Click Here</a>"
    L_LOG_START = "➜ <b>Leech Started</b>\n├─ User: {mention} ( #ID{uid} )\n└─ Source: <a href='{msg_link}'>Click Here</a>"
    
    # ===== UPLOAD MESSAGES =====
    NAME = '<b>📝 {Name}</b>\n'
    SIZE = '├─ <b>Size:</b> {Size}\n'
    ELAPSE = '├─ <b>Elapsed:</b> {Time}\n'
    MODE = '├─ <b>Mode:</b> {Mode}\n'
    
    # ----- LEECH -------
    L_TOTAL_FILES = '├─ <b>Total Files:</b> {Files}\n'
    L_CORRUPTED_FILES = '├─ <b>Corrupted:</b> {Corrupt}\n'
    L_CC = '└─ <b>By:</b> {Tag}\n\n'
    PM_BOT_MSG = '✅ <b>Files sent above in this chat</b>'
    L_BOT_MSG = '✅ <b>Files sent to Bot PM (Private)</b>'
    L_LL_MSG = '✅ <b>Files sent via Links</b>\n'
    
    # ----- MIRROR -------
    M_TYPE = '├─ <b>Type:</b> {Mimetype}\n'
    M_SUBFOLD = '├─ <b>SubFolders:</b> {Folder}\n'
    TOTAL_FILES = '├─ <b>Files:</b> {Files}\n'
    RCPATH = '├─ <b>Path:</b> <code>{RCpath}</code>\n'
    M_CC = '└─ <b>By:</b> {Tag}\n\n'
    M_BOT_MSG = '✅ <b>Links sent to Bot PM (Private)</b>'
    
    # ----- BUTTONS -------
    CLOUD_LINK = '☁️ Cloud Link'
    SAVE_MSG = '💾 Save Message'
    RCLONE_LINK = '♻️ RClone Link'
    DDL_LINK = '📎 {Serv} Link'
    SOURCE_URL = '🔐 Source'
    INDEX_LINK_F = '🗂️ Index'
    INDEX_LINK_D = '⚡ Index'
    VIEW_LINK = '🌐 View'
    CHECK_PM = '📥 Inbox'
    CHECK_LL = '🖇️ Links Log'
    MEDIAINFO_LINK = '📃 MediaInfo'
    SCREENSHOTS = '🖼️ Screenshots'
    
    # ===== STATUS DISPLAY =====
    STATUS_NAME = '📥 <b><i>{Name}</i></b>'
    BAR = '\n│ {Bar}'
    PROCESSED = '\n├─ <b>Progress:</b> {Processed}'
    STATUS = '\n├─ <b>Status:</b> <a href="{Url}">{Status}</a>'
    ETA = ' | <b>ETA:</b> {Eta}'
    SPEED = '\n├─ <b>Speed:</b> {Speed}'
    ELAPSED = ' | <b>Time:</b> {Elapsed}'
    ENGINE = '\n├─ <b>Engine:</b> {Engine}'
    STA_MODE = '\n├─ <b>Mode:</b> {Mode}'
    SEEDERS = '\n├─ <b>Seeds:</b> {Seeders} | '
    LEECHERS = '<b>Peers:</b> {Leechers}'
    
    # ===== SEEDING =====
    SEED_SIZE = '\n├─ <b>Size:</b> {Size}'
    SEED_SPEED = '\n├─ <b>Speed:</b> {Speed} | '
    UPLOADED = '<b>Uploaded:</b> {Upload}'
    RATIO = '\n├─ <b>Ratio:</b> {Ratio} | '
    TIME = '<b>Time:</b> {Time}'
    SEED_ENGINE = '\n├─ <b>Engine:</b> {Engine}'
    
    # ===== NON-PROGRESSIVE =====
    STATUS_SIZE = '\n├─ <b>Size:</b> {Size}'
    NON_ENGINE = '\n├─ <b>Engine:</b> {Engine}'
    
    # ===== FOOTER =====
    USER = '\n├─ <b>User:</b> {User} | '
    ID = '<b>ID:</b> <code>{Id}</code>'
    BTSEL = '\n├─ <b>Select:</b> {Btsel}'
    CANCEL = '\n└─ {Cancel}\n\n'
    
    FOOTER = '╔════════════════════════════════╗\n║  📊 Bot Stats 📊               ║\n╚════════════════════════════════╝\n'
    TASKS = '├─ <b>Active Tasks:</b> {Tasks}\n'
    BOT_TASKS = '├─ <b>Tasks:</b> {Tasks}/{Ttask} | <b>Free:</b> {Free}\n'
    Cpu = '├─ <b>CPU:</b> {cpu}% | '
    FREE = '<b>Disk Free:</b> {free} [{free_p}%]'
    Ram = '\n├─ <b>RAM:</b> {ram}% | '
    uptime = '<b>Uptime:</b> {uptime}'
    DL = '\n└─ <b>DL:</b> {DL}/s | '
    UL = '<b>UL:</b> {UL}/s'
    
    # ===== PAGINATION =====
    PREVIOUS = '⬅️ Previous'
    REFRESH = '🔄 [{Page}]'
    NEXT = 'Next ➡️'
    
    # ===== STOP DUPLICATE =====
    STOP_DUPLICATE = '<b>⚠️ File Already Exists in Drive!</b>\n\nHere are {content} matching results:'
    
    # ===== COUNT =====
    COUNT_MSG = '<b>🔍 Counting:</b> <code>{LINK}</code>'
    COUNT_NAME = '<b>📁 {COUNT_NAME}</b>\n'
    COUNT_SIZE = '├─ <b>Size:</b> {COUNT_SIZE}\n'
    COUNT_TYPE = '├─ <b>Type:</b> {COUNT_TYPE}\n'
    COUNT_SUB = '├─ <b>SubFolders:</b> {COUNT_SUB}\n'
    COUNT_FILE = '├─ <b>Files:</b> {COUNT_FILE}\n'
    COUNT_CC = '└─ <b>By:</b> {COUNT_CC}\n'
    
    # ===== LIST =====
    LIST_SEARCHING = '<b>🔍 Searching:</b> <i>{NAME}</i>'
    LIST_FOUND = '<b>✅ Found {NO} result(s) for:</b> <i>{NAME}</i>'
    LIST_NOT_FOUND = '<b>❌ No results found for:</b> <i>{NAME}</i>'
    
    # ===== MIRROR STATUS =====
    NO_ACTIVE_DL = '''╔════════════════════════════════╗
║  📊 No Active Tasks 📊         ║
╚════════════════════════════════╝

<b>📭 Queue is Empty</b>

Send links to start Mirror or Leech operations.

╔════════════════════════════════╗
<b>📊 Current Stats:</b>
├─ CPU: {cpu}%
├─ Disk Free: {free} [{free_p}%]
├─ RAM: {ram}%
└─ Uptime: {uptime}
╚════════════════════════════════╝'''
    
    # ===== USER SETTINGS =====
    USER_SETTING = '''╔════════════════════════════════╗
║  👤 User Settings 👤           ║
╚════════════════════════════════╝

<b>📋 Profile Information:</b>
├─ Name: {NAME} (<code>{ID}</code>)
├─ Username: {USERNAME}
├─ Telegram DC: {DC}
└─ Language: {LANG}

<b>⚙️ Setup Guide:</b>
• Use <b>-s</b> or <b>-set</b> to configure settings'''
    
    UNIVERSAL = '''╔════════════════════════════════╗
║  🌍 Universal Settings: {NAME}
╚════════════════════════════════╝

├─ YT-DLP Options: <code>{YT}</code>
├─ Daily Tasks: <code>{DT}</code> per day
├─ Last Bot Used: <code>{LAST_USED}</code>
├─ User Session: <code>{USESS}</code>
├─ MediaInfo Mode: <code>{MEDIAINFO}</code>
├─ Save Mode: <code>{SAVE_MODE}</code>
└─ Bot PM: <code>{BOT_PM}</code>'''
    
    MIRROR = '''╔════════════════════════════════╗
║  🪞 Mirror/Clone Settings: {NAME}
╚════════════════════════════════╝

├─ RClone Config: <i>{RCLONE}</i>
├─ Mirror Prefix: <code>{MPREFIX}</code>
├─ Mirror Suffix: <code>{MSUFFIX}</code>
├─ Mirror Rename: <code>{MREMNAME}</code>
├─ DDL Server(s): <i>{DDL_SERVER}</i>
├─ User TD Mode: <i>{TMODE}</i>
├─ Total User TDs: <i>{USERTD}</i>
└─ Daily Mirror: <code>{DM}</code> per day'''
    
    LEECH = '''╔════════════════════════════════╗
║  📥 Leech Settings: {NAME}
╚════════════════════════════════╝

├─ Daily Leech: <code>{DL}</code> per day
├─ Leech Type: <i>{LTYPE}</i>
├─ Custom Thumbnail: <i>{THUMB}</i>
├─ Split Size: <code>{SPLIT_SIZE}</code>
├─ Equal Splits: <i>{EQUAL_SPLIT}</i>
├─ Media Group: <i>{MEDIA_GROUP}</i>
├─ Leech Caption: <code>{LCAPTION}</code>
├─ Leech Prefix: <code>{LPREFIX}</code>
├─ Leech Suffix: <code>{LSUFFIX}</code>
├─ Leech Dumps: <code>{LDUMP}</code>
└─ Leech Rename: <code>{LREMNAME}</code>'''
