from discord.ext import commands
import discord
import random

#Star Wars Trivia Class
class Trivia(commands.Cog):
    def __init__(self, r2d2):
        self.r2d2 = r2d2

    # @commands.command()
    # async def trivia(self, ctx):
    #     global answer   

    #     await ctx.send("Welcome to Star Wars Trivia! Answer by entering the letter answer below! Let's Begin.")

    #     #Trivia Questions in the form of Question, 4 Options, Answer

    #     q1 = ["Which Star Wars movie was filmed entirely in the studio?", 
    #       "A. Star Wars",
    #       "B. Attack of the Clones",
    #       "C. Revenge of the Sith",
    #       "D. Return of the Jedi",
    #       "C"
    #       ]

    #     q2 = ["'The Star Wars Holiday Special' marked the first appearance of which Star Wars character?",
    #       "A. Bobba Fett",
    #       "B. Jar Jar Binks",
    #       "C. Jabba the Hutt",
    #       "D. Lando Calrissian",
    #       "A"
    #       ]

    #     q3 = ["Who served as Jabba the Hutt's chief of staff?",
    #       "A. Nute Gunray",
    #       "B. Maz Kanata",
    #       "C. Bib Fortuna",
    #       "D. Sarlacc",
    #       "C"
    #       ]

    #     q4 = ["Approximately how many languages can C-3PO speak?",
    #         "A. 6 Million",
    #         "B. 6 Billion",
    #         "C. 6 Trillion",
    #         "D. 6 Thousand",
    #         "A"]

    #     q5 = ["In Return of the Jedi, Jabba refers to Han as his favorite what?",
    #         "A. Knick-Knack",
    #         "B. Scoundrel",
    #         "C. Prisoner",
    #         "D. Decoration",
    #         "D"]

    #     q6 = ["What is the first Star Wars film in which Yoda is completely computer-generated?",
    #         "A. Empire Strikes Back",
    #         "B. Phantom Menace",
    #         "C. Revenge of the Sith",
    #         "D. Attack of the Clones",
    #         "D"]

    #     question_list = [q1, q2, q3, q4, q5, q6]
      
    #     #Choose a random question number from the list of questions
    #     q_num = (random.choice(question_list))                             
    #     question, opt1, opt2, opt3, opt4, answer = q_num[0], q_num[1],q_num[2],q_num[3],q_num[4], q_num[5]  
        

    #     #Ask Question/Display Options to channel
    #     await ctx.send(f'{question}\n{opt1}\n{opt2}\n{opt3}\n{opt4}\n\nType in your answer below starting with ! (for example "!A" for option A) ') 
          
    # #Recieve user input and check with answer
    # @commands.Cog.listener()
    # async def on_message(self, message):
    #   channel = message.channel
    #   if (message.author == self.r2d2.user):
    #     return
    #   if (message.content[0] == "!" and len(message.content) == 2):
    #     if (message.content[1].upper() == answer):
    #       await channel.send("Correct! I praise your galatic knowledge. Thank you for playing!")
    #       return
    #     await channel.send("Incorrect. Please prepare for the battle next time.")

#required setup def
def setup(r2d2):
    r2d2.add_cog(Trivia(r2d2))

answer = ""