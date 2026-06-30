# BrowserPassHunter 🕵️‍♂️

**浏览器密码检测工具** - 从本机浏览器中提取保存的密码、Cookie、书签和历史记录。

## 功能

✅ 自动检测已安装的浏览器
✅ 提取保存的网站密码（网站、用户名、密码）
✅ 提取 Cookie 信息
✅ 提取书签收藏
✅ 提取浏览历史记录
✅ 彩色终端输出
✅ 支持 JSON/CSV/TXT 导出
✅ 支持指定浏览器和数据类型
✅ 支持完整密码显示（--show-full-password）

## 重要说明

**Chrome v20+ 限制**: 从 Chrome 127 版本开始，Google 引入了 App-Bound Encryption（应用绑定加密），
这会阻止第三方工具直接解密保存的密码和 Cookie。对于使用 v20 加密格式的 Chrome/Edge，
本工具可以检测到密码条目但无法解密。解决方法是：

1. 直接在浏览器设置中查看密码（chrome://settings/passwords）
2. 使用旧版 Chrome（v126 及以下）
3. 或者等待工具更新以支持新的解密方式

本工具对 v10-v12 加密格式的 Chrome（127 版本以下）完全支持，可正常解密所有密码。

## 支持浏览器

### Windows

| 浏览器 | 密码 | Cookie | 书签 | 历史 |
|--------|:----:|:------:|:----:|:----:|
| Google Chrome | ✅ | ✅ | ✅ | ✅ |
| Google Chrome Beta | ✅ | ✅ | ✅ | ✅ |
| Chromium | ✅ | ✅ | ✅ | ✅ |
| Microsoft Edge | ✅ | ✅ | ✅ | ✅ |
| 360 Speed (极速) | ✅ | ✅ | ✅ | ✅ |
| 360 Safe (安全) | ✅ | ✅ | ✅ | ✅ |
| QQ Browser | ✅ | ✅ | ✅ | ✅ |
| Sogou Explorer | ✅ | ✅ | ✅ | ✅ |
| Liebao Browser | ✅ | ✅ | ✅ | ✅ |
| Cent Browser | ✅ | ✅ | ✅ | ✅ |
| 115 Browser | ✅ | ✅ | ✅ | ✅ |
| TheWorld Browser | ✅ | ✅ | ✅ | ✅ |
| Brave | ✅ | ✅ | ✅ | ✅ |
| Opera | ✅ | ✅ | ✅ | ✅ |
| OperaGX | ✅ | ✅ | ✅ | ✅ |
| Vivaldi | ✅ | ✅ | ✅ | ✅ |
| Yandex | ✅ | ✅ | ✅ | ✅ |
| CocCoc | ✅ | ✅ | ✅ | ✅ |
| Slimjet | ✅ | ✅ | ✅ | ✅ |
| Comodo Dragon | ✅ | ✅ | ✅ | ✅ |
| SRWare Iron | ✅ | ✅ | ✅ | ✅ |
| Torch Browser | ✅ | ✅ | ✅ | ✅ |
| Firefox | ✅ | ✅ | ✅ | ✅ |
| Firefox Beta | ✅ | ✅ | ✅ | ✅ |
| Firefox Dev | ✅ | ✅ | ✅ | ✅ |
| Firefox ESR | ✅ | ✅ | ✅ | ✅ |
| Firefox Nightly | ✅ | ✅ | ✅ | ✅ |

## 快速开始

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

或者单独安装：

```bash
pip install pywin32 cryptography pycryptodome
```

### 2. 运行

```bash
# 查看帮助
python browser_pass_hunter.py --help

# 提取所有浏览器密码
python browser_pass_hunter.py -p

# 提取所有数据（密码+Cookie+书签+历史）
python browser_pass_hunter.py -a

# 提取 Chrome 密码
python browser_pass_hunter.py --browser chrome -p

# 指定浏览器并提取密码和 Cookie
python browser_pass_hunter.py -b edge -p -c

# 提取所有数据并导出为 CSV
python browser_pass_hunter.py -a -e csv -o ./results

# 提取所有数据并导出为 JSON
python browser_pass_hunter.py -a -e json -o ./results

# 提取所有数据并导出为可读文本
python browser_pass_hunter.py -a -e txt -o ./results

# 提取密码并显示完整明文
python browser_pass_hunter.py -p --show-full-password
```

## 命令参数

| 参数 | 说明 |
|------|------|
| `-p, --passwords` | 提取保存的密码 |
| `-c, --cookies` | 提取 Cookie |
| `-b, --bookmarks` | 提取书签 |
| `-H, --history` | 提取浏览历史 |
| `-a, --all` | 提取所有数据 |
| `--browser <名称>` | 指定浏览器 (chrome/edge/firefox/...) |
| `--list-browsers` | 列出所有检测到的浏览器 |
| `-e json/csv/txt` | 导出数据格式 |
| `-o <目录>` | 导出目录（默认 ./browser_data） |
| `--show-full-password` | 显示完整密码（默认脱敏） |
| `--no-color` | 禁用颜色输出 |
| `-v, --version` | 显示版本号 |

## 输出示例

```
+=================================================================+
|  BrowserPassHunter v1.0.0  Browser Credential Recovery Tool|
+=================================================================+

  OS: Windows 10
  Time: 2024-01-15 14:30:00

  pywin32:     [OK]  |  cryptography: [OK]  |  pycryptodome: [OK]

= Detecting Browsers =

  Chrome-based:
    [V] Google Chrome
    [V] Microsoft Edge

  Total: 2 browser(s) detected

= Extracting Data =

  > Google Chrome (chromium)
    [V] Passwords: 5 found
    [V] Cookies: 53 found
    [V] History: 19 entries

= Summary =

  [V] Google Chrome: 5 passwords, 53 cookies, 19 history

  Total:
    Passwords: 5
    Cookies: 53
    History: 19

= Password Details =

  > Google Chrome - 5 passwords
    - https://example.com/login
      Username: user@example.com
      Password: pa********34

    - https://github.com/login
      Username: myusername
      Password: gi********xyz

  [!] Security Notice:
  This tool is for local security auditing only.
  Do not use extracted data for illegal purposes.
```

## 技术原理

### Chrome 系浏览器
- 密码存储在 `Login Data` (SQLite) 数据库中
- 使用 AES-256-GCM 加密
- 加密密钥存储在 `Local State` JSON 文件中
- 密钥由 Windows DPAPI 保护
- 通过 `CryptUnprotectData` 解密密钥，再用 AES-GCM 解密密码

### Firefox 浏览器
- 密码存储在 `logins.json` 文件中
- 加密密钥在 `key4.db` (SQLite) 中
- 使用 3DES-CBC 或 PBKDF2 派生密钥
- 需要 pycryptodome 库支持

## 安全提醒

⚠️ **本工具仅供本地安全审计使用！**

- 请勿将他人的浏览器数据用于非法用途
- 使用完毕后建议修改相关密码
- 建议定期检查浏览器中保存的密码安全性
- 本工具不会上传或发送任何数据

## 许可证

MIT License
