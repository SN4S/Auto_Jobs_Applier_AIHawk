import sqlite3
import subprocess
from subprocess import call
from datetime import datetime
from time import sleep
import app_config

def init_test_db():
    conn = sqlite3.connect(app_config.db)
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY,
    email TEXT NOT NULL UNIQUE,
    cookie TEXT,
    last_run INTEGER,
    sub_end INTEGER,
    enabled INTEGER DEFAULT TRUE)""")
    cookies = [
        {"name": "lms_ads",
         "value": "AQFCvTQco8Qc8gAAAZKcDYF7M77sg1Fq-ik0w0c8unEW3i7ggu2awGWin-iVSJe7NHtR_ZvZGaw8aN3U41_u10BGGPYfM8mu"},
        {"name": "_guid", "value": "07977a32-ce79-40d4-9abc-e8ed96702a58"},
        {"name": "bcookie", "value": "\"v=2&8a0bb844-45d6-4c40-85d4-85656a7e709f\""},
        {"name": "__cf_bm",
         "value": "rEo0kEGs4OqEKQ6xNyayhqZyW42mOJucV8WsxYWx5dg-1729196216-1.0.1.1-rW2hQNjVXaTY4AmRVCf.gKZz35kZIQDOaBhha_mZKGJBkkNPIJWKONX_YqWfgWfgIHWoKSjbzln1TtqCea8h1g"},
        {"name": "_gcl_au", "value": "1.1.1762797702.1729194978"},
        {"name": "g_state", "value": "\"i_l\":0"},
        {"name": "lms_analytics",
         "value": "AQFCvTQco8Qc8gAAAZKcDYF7M77sg1Fq-ik0w0c8unEW3i7ggu2awGWin-iVSJe7NHtR_ZvZGaw8aN3U41_u10BGGPYfM8mu"},
        {"name": "AMCVS_14215E3D5995C57C0A495C55%40AdobeOrg", "value": "1"},
        {"name": "fptctx2",
         "value": "taBcrIH61PuCVH7eNCyH0FWPWMZs3CpAZMKmhMiLe%252bH6wpXs9vi%252bBGX35czSfKfKqsoSYivJBMJHAbO9AerC%252fPsv6dzg1sUwS6XzaZbYRho3m%252bpVKpCICzVU917quCriZkJgYCG4F73agaLmldjPDRtCcplTL7YJQo8qYOhEUFubGOkZ8KI%252fv7qF1U4kRzwZRxQlLmwQAHj08lrebFmHYfhunr9TwAAb3Galoe0HuuDPUbTwjc4jSWkpzfW1f0hMmDGl3fMcs%252bs%252ftFPY7hRBbTDTKasitOSq5ORhWzYyqo1eIWbpgfxaw%252f5QwjTruwxLU60e7QDdoE4ZUawTu0vxItu23AvU%252brlRbrupyk5zHdE%253d"},
        {"name": "li_at",
         "value": "AQEDAUX4ulQEUkWFAAABkrNVqIoAAAGS12Isik0Ax9W9PCwVgv-PgMCCmBvuXlX5imf8_p6kE2V2SxCOU25W8OjEbrMLfE-bPH5bsriOd8jJqXiww0oypfODFOPWQTujUQ8_D0gzO63H9zEF7paFJDH-"},
        {"name": "lang", "value": "v=2&lang=uk-ua"},
        {"name": "lidc",
         "value": "\"b=VB32:s=V:r=V:a=V:p=V:g=4688:u=81:x=1:i=1729202612:t=1729280337:v=2:sig=AQGqOWV1t1ZNNZItaXBTQx39gw5zK77l\""},
        {"name": "aam_uuid", "value": "00229544587012512311295050128119401875"},
        {"name": "AMCV_14215E3D5995C57C0A495C55%40AdobeOrg",
         "value": "-637568504%7CMCIDTS%7C20014%7CMCMID%7C00446531336292724041240704341192703576%7CMCAAMLH-1729807413%7C6%7CMCAAMB-1729807413%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1729209813s%7CNONE%7CvVersion%7C5.1.1%7CMCCIDH%7C-444758497"},
        {"name": "AnalyticsSyncHistory",
         "value": "AQLAZ2JX9S0SyQAAAZKcDYCWjAXXLSEv7rrBedDUDkgu0WYK4xM4NT7zUId1Okkiu-wNhDU8RxCaxc4Wzsm6Tg"},
        {"name": "bscookie",
         "value": "\"v=1&20241017195616be288487-bba6-42c6-877c-e324c64a9968AQG50D1I1dcBmLgOmrZ3FqMZzdiznfXL\""},
        {"name": "dfpfpt", "value": "53181b34 9d17431fa60f0b049e7f7383"},
        {"name": "JSESSIONID", "value": "\"ajax:8972017098473961084\""},
        {"name": "li_rm",
         "value": "AQHHOSt6biubVwAAAZKcDWNQBQ6Ax6FrcIsYp8ICNVYk-_37-tDwuAQZUgVe7WUAvwQgJG2DImWoyiTTMD-2MMQeZ1OxgaG76N7MBSxtwMv8L09pW3w3UYpI"},
        {"name": "li_sugr", "value": "03374219-0b73-4106-8e38-855a5e15f1a8"},
        {"name": "li_theme", "value": "light"},
        {"name": "li_theme_set", "value": "app"},
        {"name": "liap", "value": "true"},
        {"name": "timezone", "value": "Europe/Kiev"},
        {"name": "UserMatchHistory",
         "value": "AQLNkyZs4uoHkQAAAZKcgeUX-CTx2ZPKMa6z9SO3JBirr9uJHpOfacIz0TsECMyAykjLf1ntP4pF9qToCl0ia8p2WOGOcgqlb1HZPJrHLYxZMMLCwMf-2vE2-QnVXi0xoD9PBefB6gJo42W6WJySy7IjZQGd_XeFzURDDyb6QyFNSlVIEfvDfyWuj7D70ARcivJKkbAY-ETMhKv00RAlDvBV7FNhANwpkF9TJN04qhNwE6ywFPSakE2ilvnyuRXqGP80QB16cp9RpIidoe2whUaZ6e0NgKfZ5kUu7EAcceETBT_LDIxQfX_IgTUx7NgxZ6JtKkuGTBAl6J84JAczenqZoH3s6e_PT5gXlpCKpb2W9TWtzw"}
    ]
    cookie_string = "; ".join([f'{cookie["name"]}={cookie["value"]}' for cookie in cookies])
    # cursor.execute("""INSERT INTO users (email, cookie) VALUES (?, ? )""", ("san4es772@gmail.com", cookie_string))
    cursor.execute("""CREATE TABLE IF NOT EXISTS success(
            id INTEGER PRIMARY KEY,
            user_id INTEGER NOT NULL,
            company TEXT,
            title TEXT,
            link TEXT,
            recruiter_link TEXT,
            pdf_path TEXT,
            cover_path TEXT,
            location TEXT,
            apply_date INTEGER
        )""")
    conn.commit()

def fetch_entries(dbname):
    conn = sqlite3.connect(dbname)
    cursor = conn.cursor()

    current_time_epoch = int(datetime.now().timestamp())

    query = """
        SELECT email FROM users
        WHERE last_run IS NULL OR (? - last_run) > 7200
        """

    query1 = """
        SELECT email FROM users
        WHERE ( sub_end> ? AND enabled == TRUE) AND (last_run IS NULL OR (? - last_run) > 7200)
    """

    cursor.execute(query, (current_time_epoch,))
    entries = cursor.fetchall()
    conn.close()
    return entries


while True:
    users = fetch_entries(app_config.db)
    if users:
        print("Users fetched")
        for user in users:
            try:
                subprocess.run(["python3", "main.py", "--email", f"{user[0]}"], timeout=600)
            except subprocess.TimeoutExpired as e:
                print(e)
                subprocess.call("pkill chrome", shell=True)
                sleep(1)
        users=[]
    else:
        sleep(30)
        users = fetch_entries(app_config.db)
