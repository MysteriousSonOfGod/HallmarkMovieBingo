from __future__ import print_function
import random
from mailmerge import MailMerge
import os


def create_board(board, c):
    template = 'template.docx'
    document = MailMerge(template)
    # print(document.get_merge_fields())
    document.merge(
        b0=board[0], b1=board[1], b2=board[2], b3=board[3], b4=board[4], b5=board[5], b6=board[6], b7=board[7],
        b8=board[8], b9=board[9], b10=board[10], b11=board[11], b12=board[12], b13=board[13], b14=board[14],
        b15=board[15], b16=board[16], b17=board[17], b18=board[18], b19=board[19], b20=board[20],
        b21=board[21], b22=board[22], b23=board[23], b24=board[24]
    )
    document.write(os.getcwd()+'/Boards/'+'board_{}.docx'.format(c))


def select_board_pieces(c):
    board_pieces = ["All is well in the end", "Dead Spouse", "Dead Mother", "Dead Father", "Alicia Witt", "Lacie Chabert", "Danica Mckellar",
                    "Guy Named \"Nick\"", "Mistaken Identity", "Prince/Princess Unknown", "Gingerbread", "Betty", "Baking Job/ Bakery",
                    "Terrible Graphics", "Falling into his arms", "Ice Sculpting", "Mary", "Holly", "Inn with X-mas theme", "LSC: Overwork",
                    "LSC: Death", "LSC: Depressing Upbringing", "Bookstore", "Overbearing Boyfriend", "Overbearing Girlfriend",
                    "Town with Christmas Name", "Amnesia", "Restaurateur", "Run into her/him", "Wake up to new life", "Bell Ringing Santa",
                    "Magical Santa", "Unknown Country", "Secret Santa", "Candace Cameron Barae", "Working in Advertising", "Mean Rich Parents",
                    "Bad acting child", "Depressing Town", "Peppermint Latte/Hot Chocolate", "Famous person in small town", "Better looking co-star",
                    "Former Fiance", "Gazebo", "Working through holidays", "Laugh out loud (Not you)", "Mistaken Parentage", "Actual Santa",
                    "Pretend to be dating", "Inspiring Mom", "Inspiring Dad", "Divorce", "Carolers strolling or in costume", "Snowball Fight",
                    "Competing man/woman", "Family business expectations", "Totally fake snow", "Needing $$$ through contest", "\"The\" Ice rink",
                    "LSC: Bad Romance", "Blatant Product Placement"]

    board_array = random.sample(range(1, len(board_pieces)), 25)
    board_array[12] = 0
    final_board = [board_pieces[i] for i in board_array]
    # print(final_board)
    create_board(final_board, c)


def remove_and_create_boards(num_players):
    # Remove previous boards
    for file in os.listdir(os.getcwd()+'\\Boards'):
        if file.startswith("board"):
            try:
                os.remove(os.getcwd()+'\\Boards\\'+file)
            except FileNotFoundError:
                print("File to delete not found..")
                pass
    count = 0
    for x in range(int(num_players)):
        select_board_pieces(count)
        count += 1
    print("{} boards written to {}\\Boards. ".format(count, os.getcwd()))
