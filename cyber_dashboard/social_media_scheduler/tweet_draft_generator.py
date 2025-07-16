import time
from datetime import datetime, timedelta

def read_tweets(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return [line.strip() for line in file if line.strip()]

def generate_schedule(tweets, delay_seconds=120):
    now = datetime.now()
    schedule = []

    for i, tweet in enumerate(tweets):
        post_time = now + timedelta(seconds=i * delay_seconds)
        schedule.append((post_time.strftime("%Y-%m-%d %H:%M:%S"), tweet))

    return schedule

def save_drafts(schedule, filename='scheduled_tweets.txt'):
    with open(filename, 'w', encoding='utf-8') as file:
        for timestamp, tweet in schedule:
            file.write(f"{timestamp} - {tweet}\n")
    print(f"✅ Drafts saved to {filename}")

if __name__ == "__main__":
    tweets = read_tweets('tweets.txt')
    if not tweets:
        print("No tweets found in tweets.txt")
    else:
        schedule = generate_schedule(tweets, delay_seconds=120)
        save_drafts(schedule)
