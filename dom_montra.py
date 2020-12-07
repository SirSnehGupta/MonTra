#importing pre-existing modules.
import sys
import dom_csv_creation as cc

#importing other required modules and advising the user to install missing modules(if any).
try:
    import matplotlib.pyplot as plt
    import pandas as pd
    import tabulate as tb
except:
    print("Please install the required modules:\nMatplotlib\nPandas\nTabulate\n")
    sys.exit()
#defining MonTra Household Edition's core function
def d_montra():
    cc.create_file()        #calling the function to check whether the CSV files are pre-existing or not.
                            #if not, creating the required CSV files.

    file = open('help.txt','r')
    inc = pd.read_csv('dom_income.csv', index_col=0)        #opening help.txt file in reading mode.
    exp = pd.read_csv('dom_expense.csv', index_col=0)       #fetching income/expense data from the CSV files.

    #Welcome message.
    print("\nWelcome to MonTra Household Edition\nA Simple yet efficient CLI-Based Finance-Tracker for your household.")
    print("Currency is assumed as per user's preference.")

    #declaring lists and other attributes for minimal error encounters for users that may lead to crashing of the program.
    mnt = ['Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec','Jan','Feb','Mar']
    incl = ['Earnings','Interest_on_Investments','Dividend','Rent','Other_inc']
    expl = ['Housing','Electricity','Telecom','Groceries','Entertainment','Healthcare','Insurance','Tax','Other']
    sym = ['=','+','-','*','/']
    syn_er = "There's a syntax error in your command, please recheck."
    edit = False
    saved = 1

    while True:
        cmd = input('\nMonTra λ ')      #MonTra's command prompt.
        cmdl = cmd.split()              #splitting the command into lists to enable processing of the command.
        suc = 0                         #initializing error and success scores.
        err = 0

        try:                                            #Try and Except block for editing commands.
            if cmdl[0] == 'income' and len(cmdl) == 7:  #command structure check.
                if cmdl[2] in mnt and cmdl[4] in incl and cmdl[5] in sym and cmdl[1] == ':' and cmdl[3] == ':' and type(float(cmdl[6])) is float:
                    if cmdl[5] == '=':
                        inc.loc[cmdl[2],cmdl[4]] = float(cmdl[6])
                        print(tb.tabulate(inc, headers = 'keys', tablefmt = 'psql'))
                    elif cmdl[5] == '+':    
                        inc.loc[cmdl[2],cmdl[4]] += float(cmdl[6])
                        print(tb.tabulate(inc, headers = 'keys', tablefmt = 'psql'))
                    elif cmdl[5] == '-':    
                        inc.loc[cmdl[2],cmdl[4]] -= float(cmdl[6])
                        print(tb.tabulate(inc, headers = 'keys', tablefmt = 'psql'))
                    elif cmdl[5] == '*':    
                        inc.loc[cmdl[2],cmdl[4]] *= float(cmdl[6])
                        print(tb.tabulate(inc, headers = 'keys', tablefmt = 'psql'))
                    elif cmdl[5] == '/':    
                        inc.loc[cmdl[2],cmdl[4]] /= float(cmdl[6])
                        print(tb.tabulate(inc, headers = 'keys', tablefmt = 'psql'))
                    suc = 1                             #Redifining certain attributes.  
                    edit = True
                    saved = 0
                    
                else:
                    print(syn_er)                       #prints syntax error message for invalid command input.
                    err = 1
                
            elif cmdl[0] == 'expense' and  len(cmdl) == 7:
                if cmdl[2] in mnt and cmdl[4] in expl and cmdl[5] in sym and cmdl[1] == ':' and cmdl[3] == ':' and type(float(cmdl[6])) == float:
                    if cmdl[5] == '=':
                        exp.loc[cmdl[2],cmdl[4]] = float(cmdl[6])
                        print(tb.tabulate(exp, headers = 'keys', tablefmt = 'psql'))
                    elif cmdl[5] == '+':    
                        exp.loc[cmdl[2],cmdl[4]] += float(cmdl[6])
                        print(tb.tabulate(exp, headers = 'keys', tablefmt = 'psql'))
                    elif cmdl[5] == '-':    
                        exp.loc[cmdl[2],cmdl[4]] -= float(cmdl[6])
                        print(tb.tabulate(exp, headers = 'keys', tablefmt = 'psql'))
                    elif cmdl[5] == '*':    
                        exp.loc[cmdl[2],cmdl[4]] *= float(cmdl[6])
                        print(tb.tabulate(exp, headers = 'keys', tablefmt = 'psql'))
                    elif cmdl[5] == '/':    
                        exp.loc[cmdl[2],cmdl[4]] /= float(cmdl[6])
                        print(tb.tabulate(exp, headers = 'keys', tablefmt = 'psql'))
                    suc = 1
                    edit = True
                    saved = 0

                else:
                    print(syn_er)
                    err = 1

        except ValueError:
            print(syn_er)                               #ValueError handling to warn user and avoid crashing.
            err = 1
        except IndexError:
            print("'' - not a command, try again.")     #IndexError handling to warn user and avoid crashing.
            err = 1
        try:                                            #Try and Except block for other commands.
            if cmdl[0] == 'credits':                    #command to show credits.
                print("Developers:")
                print("Sneh Gupta\tYash Patel\tDhruvil Joshi")           
                    
            elif cmdl[0] == 'save':                     #command to save changes.
                inc.to_csv('dom_income.csv')
                exp.to_csv('dom_expense.csv')
                saved = 1                               #redifining certain attributes
                edit = False

            elif cmdl[0] == 'help':                     #command for help which reads out help.txt.
                print(file.read())

            elif cmdl[0] == 'show':                     #command to show the tables.
                print("INCOME Table\n", tb.tabulate(inc, headers = 'keys', tablefmt = 'psql'))      #displaying the tables in PostgreSQL table
                print("EXPENSE Table\n", tb.tabulate(exp, headers = 'keys', tablefmt = 'psql'))     #format with the help of 'tabulate' module.

            elif cmdl[0] == 'plot':                     #command to plot income and expense heads.
                alls = input('Mention income/expense category(ies)(separate them by space) which you wish to observe graphically: ')
                lall = alls.split()
                if len(lall) == 0:
                    print("'' - invalid income/expense")
                elif len(lall) > 0:
                    for items in lall:
                        if items in incl:
                            plt.plot(mnt, list(inc[items]), label = items)
                            plt.xlabel('Months')
                            plt.ylabel('Amount')
                            plt.legend()
                        elif items in expl:
                            plt.plot(mnt, list(exp[items]), label = items)
                            plt.xlabel('Months')
                            plt.ylabel('Amount')
                            plt.legend()
                        elif items not in incl and items not in expl:
                            print('Invalid income/expense selection')
                    plt.show()
                
            elif cmdl[0] == 'exit':                     #command to exit to main menu.
                if saved == 1 and edit == False:        #if the tables are saved and no further edits.
                    print("Exiting...\nDone")           #are made, it exits straight away.
                    break
                else:                                   #if the above condition is not satisfied, it asks
                    while True:                         #whether to save and exit or not.
                        save = input('Save and exit?[Y/n]: ')
                        if save == 'n':
                            print('Exiting...\nDone')
                            break
                        elif save == 'y' or save == 'Y' or save == '':
                            print('Saving and exiting...\nDone')
                            inc.to_csv('dom_income.csv')
                            exp.to_csv('dom_expense.csv')
                            break
                        else:
                            print('Invalid selection')  
                    break

            else:
                if err == 1 or suc == 1:            #if there is already an error message given, it'll
                    pass                            #not give this error(with reference to previous Try
                else:                               #and Except block).
                    print("'"+cmd+"'-",'not a command, try again.')
        except IndexError:
            pass                                    #IndexError handling to avoid crashing.

if __name__ == '__main__':                          #if this file is run as main, run the core function.
    d_montra()