embed = discord.Embed(title="Need help?",
                      description="Looking for a way to contact me? Curious about commission details? Need to get support for my products, plugins or setups? You're in the right place.",
                      colour=0x40ff49,
                      timestamp=datetime.now())

embed.set_author(name="Filip (filipeex) Karab",
                 icon_url="https://drive.google.com/uc?id=1ffbE0t7dY6NDVHgWuGpgQiN03eipXO2T")

embed.add_field(name="Who am I?",
                value="> `Hello, my full name is Filip Karab, but I mostly go by just `*`Filip`*`. I do freelance work on Fiverr (custom minecraft plugins, setups or even custom games) and I also make publicly available top-quality plugins and setups. I'm currently 16yo and live in Slovakia.`",
                inline=False)
embed.add_field(name="What is this server?",
                value="> `This is a place to look for support, contact me through a ticket, or just chat with other clients and members. I like to refer to it as `*`my cave`*`. Down below you can see a few ways to view my work, or contact me.`",
                inline=False)
embed.add_field(name="See my work on GitHub.",
                value="> `You can look through my public repositories `[`here`](https://github.com/FilipeeX)`. There's like 7 of them and some of them are very much old, but I recommend going through the pinned ones.`",
                inline=True)
embed.add_field(name="Reach out to me directly, create a ticket.",
                value="> `You can always create a ticket for any matter, just follow the tutorial in `<#1186241213158916166>`.`",
                inline=True)

embed.set_footer(text="Hope you have a great day - Filip :)")