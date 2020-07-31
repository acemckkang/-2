import discord
import asyncio
from urllib.request import urlopen
from urllib import parse
import datetime
from discord.utils import get
import random
client = discord.Client()
token = "NzA0OTMzOTA0MjA5MTUwMDMy.XrjNpw._xvRR8nD_nhO2v3l0p7AVXgsKpU"
guild_list = client.guilds
@client.event
async def on_ready():
	a=len(client.guilds)
	game = discord.Game(f"{a}개의 서버에 접속 중....")
	print("========================")
	print("다음으로 로그인 합니다 : ")
	print(client.user.name)
	print("connection was successful")
	print("=========================")
	for i in range (len(client.guilds)):
			print(client.guilds[i])
	await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
	ids = message.author.id #id라는 변수에는 메시지를 보낸사람의 ID를 담습니다.
	channel = message.channel #channel이라는 변수에는 메시지를 받은 채널의 ID를 담습니다.
	if message.author.bot:
		return None

	elif message.content.startswith("에이스봇 킥"):
            if message.author.guild_permissions.kick_members:
                userid = message.content[7:]
                user_id = re.findall("\d+", userid)
                userkick = message.guild.get_member(int(user_id[0]))
                await message.guild.kick(userkick)
                await message.channel.send(str(userkick) + "님을 추방했습니다")


    elif message.content.startswith("에이스봇 채팅청소"): 
        if message.author.guild_permissions.manage_messages:
            try:
                amount = message.content[10:]
                await message.channel.purge(limit=int(amount))
                await message.channel.send(f"**{amount}**개의 메시지를 지웠습니다.")
            except ValueError:
                    await message.channel.send("청소하실 메시지의 **수**를 입력해 주세요.")
        else:
            await message.channel.send("권한이 없습니다.")

	elif message.content.startswith("에이스봇 안녕?"):
		await message.channel.send(f'안녕하세요! {message.author}님. 추천은 해주실거죠?  링크:https://top.gg/bot/704933904209150032')

	elif message.content.startswith("에이스봇 서버수"):
		a=len(client.guilds)
		await message.channel.send(f"{a}개의 서버에 접속 중...")

	elif message.content.startswith("에이스봇 설명"):
		embed = discord.Embed(title="에이스봇ver.1.3", description="전 디스코드의 에이스#4001 님이 만든 디스코드 봇 입니다..", color=0x00ff00)
		embed.set_footer(text="@here https://koreanbots.dev/bots/704933904209150032 이 링크로 들어가서 좋아요 눌러주세요.")
		await message.channel.send(embed=embed)

	elif message.content.startswith("에이스봇 뭐해?"):
		await message.channel.send(f"{message.author}님,""전 지금 대화중이에요.")

	elif message.content.startswith("에이스봇 넌 누구니?"):
		await message.channel.send("전 에이스#4001 님이 만든 디스코드 봇이에요.")
	
	elif message.content.startswith("에이스봇 바보"):
		await message.channel.send(f'바보는 {message.author} 님이죠.')

	elif message.content.startswith("에이스봇 DM"):
		author=message.guild.get_member(int(message.content[8:26]))
		msg=message.content[27:]
		q=message.author
		tit=f"{q}님의 메세지"
		embed=discord.Embed(title=tit, description=msg, color=0x00ff00)
		embed.set_footer(text="파이썬을 이용해 만들었어요.")
		await author.send(embed=embed)
		await message.channel.send("DM메세지 보내기를 완료하였습니다.")

	elif message.content.startswith("에이스봇 게임"):
		await message.channel.send('''크런커 한판 하실래요?
	https://krunker.io/?game=TOK:cpw16''')

	elif message.content.startswith("에이스봇 하이퍼링크"):
        embed = discord.Embed(title="하이퍼링크", description=['링크 메시지']('https://acemckkang.github.io/codingcenter/홈페이지.html'), color='0x00ff00')
		await message.channel.send(embed=embed)

	elif message.content.startswith("에이스봇 따라해"):
		replay = message.content[9:]
		await  message.channel.send(replay)

	elif message.content.startswith("에이스봇 초대링크"):
		await message.channel.send('''여기 초대링크에요!
	https://discord.com/api/oauth2/authorize?client_id=704933904209150032&permissions=0&redirect_uri=https%3A%2F%2Fdiscord.gg%2Fk7QQCrf&scope=bot''')

	elif message.content.startswith("에이스봇 도움말"):
		embed = discord.Embed(title="에이스봇ver.1.3 도움말", description='''
			에이스봇 초대링크
			에이스봇 따라해(할말)
			에이스봇 핑
			에이스봇 도박 (돈)
			에이스봇 뮤트 (아이디) #이 기능은 '뮤트'라는 역할을 추가하고 그 역할의 메세지 권한을 없애야 해요.
			에이스봇 언뮤트 (아이디)
			에이스봇 DM (아이디)
			에이스봇 설명 라고 입력해 보세요.''', color=0x00ff00)
		embed.set_footer(text="파이썬을 이용해 만들었어요.")
		await message.channel.send(embed=embed)

	elif message.content.startswith('에이스봇 핑'):
		embed = discord.Embed(title="에이스봇 현재 핑", description='현재 핑:{0}'.format(round(client.latency*1000))+'ms  상태:매우 양호',color=0x03ff00)
		embed.set_footer(text='''에이스봇을 추천해주세요. 
링크:https://top.gg/bot/704933904209150032''')
		await message.channel.send(embed=embed)

	elif message.content.startswith("에이스봇 도박"):
		embed = discord.Embed(title="에이스봇 도박", description='''
			도박중...''', color=0x00ff00)
		embed.set_footer(text="에이스봇 도박기능을 많이 이용해주세요!")
		await message.channel.send(embed=embed)
		money=message.content[8:]
		ss=random.randint(1,10)
		dd=random.randint(1,10)
		embed = discord.Embed(title="에이스봇 도박 결과", description=f'''
		에이스봇의 카드는 {ss}!
		{message.author}님의 카드는 {dd}!
		''', color=0x00ff00)
		embed.set_footer(text="파이썬을 이용해 만들었어요.")
		await message.channel.send(embed=embed)
		em=discord.Embed(title="도박 승리", description=f'''
			도박에서 승리하였습니다.  {money}원을 얻었습니다.''', color=0x00ff00)
		embed.set_footer(text="파이썬을 이용해 만들었어요.")
		bed=discord.Embed(title="도박 패배", description=f'''
			도박에서 패배하였습니다.  {money}원을 잃었습니다.''', color=0x00ff00)
		embed.set_footer(text="파이썬을 이용해 만들었어요.")
		if dd>ss:
			await message.channel.send(embed=em)
		else:
			await message.channel.send(embed=bed)



	elif message.content.startswith("에이스봇"):
		 dsds= message.content[4:]
		 await message.channel.send(f"{dsds}(이)가 무슨 뜻인지 모르겠어요.")
		 await message.channel.send("https://koreanbots.dev/bots/704933904209150032 이 링크로 들어가서 좋아요 눌러주세요.")
			
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.offline)
    print(client.user.id)
    print("ready")
    game = discord.Game("시작하는 중...")
    await client.change_presence(status=discord.Status.online, activity=game)
    while True:
        game = discord.Game("이제 DM메세지 기능을 이용할 수 있어요!")
        await client.change_presence(status=discord.Status.online, activity=game)
        await asyncio.sleep(3)
        game = discord.Game("'에이스봇 도움말' 이라고 입력해 보세요.")
        await client.change_presence(status=discord.Status.online, activity=game)
        await asyncio.sleep(3)
        ch = len(client.users)
        game = discord.Game("{}명의 사용자와 함께하는 중입니다".format(ch))
        await client.change_presence(status=discord.Status.online, activity=game)
        await asyncio.sleep(3)
        game = discord.Game("뮤트 기능은 삭제되었습니다.")
        await client.change_presence(status=discord.Status.online, activity=game)
        await asyncio.sleep(3)
        ch = len(client.guilds)
        game = discord.Game("{}개의 서버에 접속 중...".format(ch))
        await client.change_presence(status=discord.Status.online, activity=game)
        await asyncio.sleep(3)
        game = discord.Game("에이스봇 지원 서버:https://discord.gg/9anFyMJ")
        await client.change_presence(status=discord.Status.online, activity=game)
        await asyncio.sleep(3)
client.run(token)
