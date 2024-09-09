import discord
import json
import asyncio
import random

# Discord 봇 토큰
TOKEN = 'put you are bot token'

# 변경할 닉네임 목록이 있는 JSON 파일 경로
NICKNAMES_FILE = "nicks.json"

# 대상 유저 ID
TARGET_USER_ID = 964496241075585034

# 닉네임 변경 주기 (초)
INTERVAL = 120  # 2분

client = discord.Client(intents=discord.Intents.all())


async def change_nickname():
    await client.wait_until_ready()

    try:
        with open(NICKNAMES_FILE, "r", encoding="utf-8") as f:
            nicknames = json.load(f)
    except FileNotFoundError:
        print(f"닉네임 목록 파일 '{NICKNAMES_FILE}'을 찾을 수 없습니다.")
        return

    guild = client.get_guild(1115602619084312647)  # GUILD_ID를 서버 ID로 변경해야 합니다.
    member = guild.get_member(TARGET_USER_ID)

    if member:
        while True:
            new_nickname = random.choice(nicknames)
            try:
                await member.edit(nick=new_nickname)
                print(f"닉네임을 '{new_nickname}'으로 변경했습니다.")
            except discord.HTTPException as e:
                print(f"닉네임 변경 실패: {e}")
            await asyncio.sleep(INTERVAL)
    else:
        print(f"서버에서 유저를 찾을 수 없습니다. (ID: {TARGET_USER_ID})")


@client.event
async def on_ready():
    print(f"{client.user}로 로그인했습니다.")
    client.loop.create_task(change_nickname())


client.run(TOKEN)
