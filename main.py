# 1. import required modules
# Copyright 2023 Max Cieplinski. All rights reserved. You are granted the right to distribute this software, with proper attribution.
#Sounds courtesy of Mixkit.
from tkinter import *
from tkinter.messagebox import *
import simpleaudio as sa
class ClickerGame:
    def __init__(self):
        self.clicks = 0
        self.awards_earned = []
        self.window = Tk()
        self.window.config(background="green")
        self.window.title(f"Clicker World | Clicks: {self.clicks}")
        self.awards = {"50": "Novice", "100": "Beginner", "150": "Good Start", "200": "Picking up steam", "250": "Skillful", "300": "Smart", "350": "Awesome", "400": "Epic", "450": "On a roll", "500": "Keep 'em coming", "550": "Click away darlin'", "600": "Magical", "650": "Keep clickin' for the history books.", "700": "Impossible!", "750": "Now you're cooking with gas", '800': "I think i'll faint", "850": f"This guy's insane. His cps is insane. Amirite?", "900": "You're breeezing through this", "950": "Almost there. Don't give up now!", "1000": "You did it!"}
        self.AutoClickerPrices = {
            "Cursor": 100,
            "Mine": 500,
            "Money Farm": 1000,
            "Click Factory": 2000,
            "AutoHarvester": 5000,
            "Diamond Clicker": 10000,
            "Golden Touch": 20000,
            "Platinum Automator": 50000,
            "Ultimate Clicker": 100000,
            "Epic AutoMaster": 200000
        }
        self.AutoClickeradds = {
            "Cursor": 5,
            "Mine": 20,
            "Money Farm": 50,
            "Click Factory": 80,
            "AutoHarvester": 100,
            "Diamond Clicker": 300,
            "Golden Touch": 500,
            "Platinum Automator": 1000,
            "Ultimate Clicker": 5000,
            "Epic AutoMaster": 100000
        }
        self.ClickerUpdate = 0
        self.window.geometry("300x350")
        background_image = PhotoImage("/Users/max/Downloads/DALL·E 2023-02-12 14.06.49 - An detailed pixel art style dungeons and dragons style video game map.png")

        background_label = Label(self.window, image=background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.Clicker = Button(self.window, text="Click to increment clicks.", background="green", command=self.update)
        self.destroyer = Button(self.window, text="Leave game", fg="red", bg="red", command=self.close)
        self.info = Label(self.window, text=f"Clicks: {str(self.clicks)}", font="black")
        self.shopButton = Button(self.window, text="Purchase Auto Clickers", fg="green", command=self.shop)
        self.what_to_buy = Entry(self.window, width=20, fg="white")
        self.Clicker.pack()
        self.destroyer.pack()
        self.info.pack()
        self.shopButton.pack()
        self.what_to_buy.pack()
        self.window.mainloop()
        # 2. define functions
    def update(self):
        print("You clicked once.")
        self.clicks = self.clicks + 1
        self.clicks = self.clicks + self.ClickerUpdate
        self.info.config(text=f"Clicks: {self.clicks}")
        self.info.pack()
        self.window.title(f"Clicker World | Clicks: {self.clicks}")
        for level in list(self.awards.keys()):
            if self.clicks >= int(level) and level not in self.awards_earned:
                self.awards_earned.append(level)
                wave_obj = sa.WaveObject.from_wave_file(
                    "/Users/max/PycharmProjects/ClickerGame/mixkit-achievement-bell-600.wav")
                play_obj = wave_obj.play()
                play_obj.wait_done()
                print(f"Congratulations! You achieved the rank {self.awards[str(self.clicks)]}.")
                if self.clicks == 1000:
                    wave_obj = sa.WaveObject.from_wave_file(
                        "/Users/max/PycharmProjects/ClickerGame/mixkit-birthday-crowd-party-cheer-531.wav")
                    play_obj = wave_obj.play()
                    play_obj.wait_done()
                showinfo("Award won!",
                         f"You clicked the button {self.clicks} times. That gives you the rank {self.awards[str(self.clicks)]}. Congratulations!")



    def close(self):

        answer = askyesno("Leave?", "Are you sure you want to leave Clicker world?")
        if answer:
            print("You will now leave Clicker World.")
            showinfo("Exit", "You will now leave Clicker World. Bye! 👋")
            print("You clicked the button " + str(self.clicks) + " times. Congratulations!")
            self.window.destroy()
        else:
            print("You will not be exited.")
            showinfo("Not leaving Clicker World:", "You have not been exited from Clicker World.")

    def shop(self):
        print("You have selected the shop button.")
        showinfo("Shop Starting...", "The Auto Clicker Shop is now opening.")
        showinfo("Available Auto Clickers", f"Available Auto Clickers: {list(self.AutoClickeradds.keys())}")
        showinfo("Place to enter choice", "To enter your preferred option, look at the console.")
        answer = input("What Auto Clicker do you want?")
        try:
            price = self.AutoClickerPrices[answer]
            if price <= self.clicks:
                purchase = askyesno("Clicks Sufficent.", f"You have enough clicks to purchase. You would have {self.clicks - price} clicks remaining. Would you like to buy {answer}?")
                if purchase:
                    self.clicks = self.clicks - price
                    self.window.title(f"Clicker World | Clicks: {self.clicks}")
                    self.ClickerUpdate = self.ClickerUpdate + self.AutoClickeradds[answer]
                    showinfo("Purchase Success", f"Purchase successful! You now have {self.clicks} clicks.")
                else:
                    print("OK. Bye!")
                    showinfo("Leaving Dialog", "Bye! We look forward to seeing you.")
            else:
                showinfo("Insufficient Clicks", f"Oh no! You do not have enough clicks for that autoclicker! You need {price - self.clicks} more clicks. Please check back later. Bye!")

        except KeyError:
            showinfo("Invalid Auto Clicker.", "The auto clicker you selected does not exist.")
    def __str__(self):
        return "This is a clicker game powered by tkinter. It was made by Max Cieplinski."
myclick = ClickerGame()



