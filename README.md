# 🤖 AutoCommit Bot

Keep your GitHub contribution graph consistently active with this automated Python tool. Perfect for maintaining streaks or showcasing regular activity on your profile.

## 🌟 Features

- Automated daily commits with timestamps
- Natural-looking activity patterns with randomized delays
- Customizable commit messages
- Multiple commits per execution (3-5 commits each run)
- Detailed logging system for tracking and debugging
- Easy setup with minimal configuration

## 🚀 Getting Started

### Prerequisites

- Python 3.x
- `gitpython` library
- GitHub account and repository

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/autocommit-bot.git
   cd autocommit-bot
   ```

2. Install required dependencies:
   ```bash
   pip install gitpython
   ```

3. Configure Git with your credentials:
   ```bash
   git config --global user.name "Your Name"
   git config --global user.email "your-email@example.com"
   ```

## 💻 Usage

### Manual Execution

Navigate to the repository directory and run:
```bash
python3 auto_commit.py
```

### Automated Execution (Cron)

1. Open crontab:
   ```bash
   crontab -e
   ```

2. Add a daily schedule (example: run at 9 AM):
   ```bash
   0 9 * * * /path/to/python3 /path/to/autocommit-bot/auto_commit.py >> /path/to/autocommit-bot/cron_output.log 2>&1
   ```

## ⚙️ Customization

### Commit Messages

Edit the `commit_messages` list in `auto_commit.py`:
```python
commit_messages = [
    "Update activity log 📄",
    "Daily log entry 📝",
    "Streak saver 🔥",
    "Keep the streak alive 💪",
    "Refresh log file 🕒"
]
```

### Commit Settings

Adjust frequency and timing in `auto_commit.py`:
```python
# Number of commits per execution
num_commits = random.randint(3, 5)

# Delay between commits (seconds)
delay = random.randint(10, 60)
```

## 📝 Logging

The script maintains a `cron_debug.log` file containing:
- Commit timestamps
- Selected messages
- Delay durations
- Error reports

## 🔧 Troubleshooting

### Common Issues

1. **Commits not appearing on GitHub:**
   - Verify email matches GitHub account
   - Check repository visibility
   - Ensure pushing to correct branch

2. **Script errors:**
   - Review `cron_debug.log`
   - Verify Python and Git installation
   - Check file permissions

## ⚠️ Disclaimer

This tool is for educational and personal use. Please use responsibly and in accordance with GitHub's Terms of Service.

## 🤝 Contributing

Contributions welcome! Feel free to:
- Fork the repository
- Create a feature branch
- Submit a pull request

## 📄 License

This project is licensed under the MIT License.

---

Made with ❤️ by Vir Khanna