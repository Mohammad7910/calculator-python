from tkinter import *
from math import *
from tkinter import ttk
from tkinter import messagebox

win = Tk ( )
win.title ( "Calculator" )
win.geometry ( "500x500" )
win.config ( bg = "pink" )
lb = ttk.Label ( win , text = "Welcome To" )
lb.place ( x = 165 , y = 70 )
lb.config ( font = ("b nazanin" , 20 , "bold") , background = "pink" )
lb1 = ttk.Label ( win , text = "Math Calculator" )
lb1.place ( x = 100 , y = 110 )
lb1.config ( font = ("impact" , 34) , background = "pink" )


# CALCULATOR
def calculator ( ):
    tl = Toplevel ( win )
    tl.geometry ( "600x500" )
    tl.title ( "Calculator" )
    tl.config ( bg = "light green" )
    btn = ttk.Button ( tl , text = "exit" , command = tl.destroy )
    btn.place ( x = 400 , y = 30 )

    # FIRST ENTRY
    lb1 = ttk.Label ( tl , text = "First Num: " )
    lb1.place ( x = 130 , y = 20 )
    FN = ttk.Entry ( tl )
    FN.place ( x = 200 , y = 20 )

    # SECOND ENTRY
    lb2 = ttk.Label ( tl , text = "Second Num: " )
    lb2.place ( x = 112 , y = 50 )
    SN = ttk.Entry ( tl )
    SN.place ( x = 200 , y = 50 )

    # RESULT
    lb3 = ttk.Label ( tl , text = "Result : " )
    lb3.place ( x = 140 , y = 80 )

    # =============================SUM=================================
    def sum ( ):
        lb = ttk.Label ( tl )
        lb.place ( x = 200 , y = 80 )
        try:
            lb.config ( text = float ( FN.get ( ) ) + float ( SN.get ( ) ) , width = 30 )
        except:
            pass

    btn = Button ( tl , text = "sum(+)" , command = sum )
    btn.place ( x = 20 , y = 120 , width = 80 , height = 80 )
    btn.config ( fg = "blue" , bg = "yellow" )

    # ====================================DEDUCT===========================
    def deduct ( ):
        lb = ttk.Label ( tl )
        lb.place ( x = 200 , y = 80 )
        try:
            lb.config ( text = float ( FN.get ( ) ) - float ( SN.get ( ) ) , width = 30 )
        except:
            pass

    btn = Button ( tl , text = "deduct(-)" , command = deduct )
    btn.place ( x = 110 , y = 120 , width = 80 , height = 80 )
    btn.config ( fg = "blue" , bg = "yellow" )

    # =============================MULTIPLY=============================
    def multiply ( ):
        lb = ttk.Label ( tl )
        lb.place ( x = 200 , y = 80 )
        try:
            lb.config ( text = float ( FN.get ( ) ) * float ( SN.get ( ) ) , width = 30 )
        except:
            pass

    btn = Button ( tl , text = "multiply(*)" , command = multiply )
    btn.place ( x = 20 , y = 220 , width = 80 , height = 80 )
    btn.config ( fg = "blue" , bg = "yellow" )

    # =============================DIVIDE========================
    def divide ( ):
        lb = ttk.Label ( tl )
        lb.place ( x = 200 , y = 80 )
        lb = ttk.Label ( tl )
        lb.place ( x = 200 , y = 80 )
        try:
            lb.config ( text = float ( FN.get ( ) ) / float ( SN.get ( ) ) , width = 30 )
        except:
            messagebox.showerror ( "Value Error" , "There is A Value Error!!" )

    btn = Button ( tl , text = "divide(/)" , command = divide )
    btn.place ( x = 110 , y = 220 , width = 80 , height = 80 )
    btn.config ( bg = "black" , fg = "white" )

    # =================================INT DIVIDE=========================
    def int_divide ( ):
        lb = ttk.Label ( tl )
        lb.place ( x = 200 , y = 80 )
        lb = ttk.Label ( tl )
        lb.place ( x = 200 , y = 80 )
        try:
            lb.config ( text = float ( FN.get ( ) ) // float ( SN.get ( ) ) , width = 30 )
        except:
            messagebox.showerror ( "Value Error" , "There is A Value Error!!" )

    btn = Button ( tl , text = "int divide(//)" , command = int_divide )
    btn.place ( x = 20 , y = 310 , width = 80 , height = 80 )
    btn.config ( fg = "blue" , bg = "yellow" )

    # =================================POWER===========================
    def power ( ):
        lb = ttk.Label ( tl )
        lb.place ( x = 200 , y = 80 )
        try:
            lb.config ( text = float ( FN.get ( ) ) ** float ( SN.get ( ) ) , width = 30 )
        except:
            pass

    btn = Button ( tl , text = "power(**)" , command = power )
    btn.place ( x = 110 , y = 310 , width = 80 , height = 80 )
    btn.config ( bg = "black" , fg = "white" )

    # =================================GREAT COMMON DIVISOR=========================
    def great_common_divisor ( ):
        lb = ttk.Label ( tl )
        lb.place ( x = 200 , y = 80 )
        try:
            lb.config ( text = gcd ( int ( FN.get ( ) ) , int ( SN.get ( ) ) ) , width = 30 )
        except:
            pass

    btn = Button ( tl , text = "GCD\n(great\ncommon\ndivisor)" , command = great_common_divisor )
    btn.place ( x = 20 , y = 400 , width = 80 , height = 80 )
    btn.config ( fg = "blue" , bg = "yellow" )

    # =================================SQUARE ROOT==============================
    def square_root ( ):
        lb = ttk.Label ( tl )
        lb.place ( x = 200 , y = 80 )
        try:
            lb.config ( text = sqrt ( float ( FN.get ( ) ) ) , width = 30 )
        except:
            messagebox.showerror ( "Value Error" ,
                                   "There is A Value Error!!\nThe Negative Numbers Don't Have Square Root!!" )

    btn = Button ( tl , text = "√\n(square root)" , command = square_root )
    btn.place ( x = 110 , y = 400 , width = 80 , height = 80 )
    btn.config ( fg = "blue" , bg = "yellow" )

    # ==================================LOG10========================================
    def log ( ):
        lb = ttk.Label ( tl )
        lb.place ( x = 200 , y = 80 )
        try:
            lb.config ( text = log10 ( float ( FN.get ( ) ) ) , width = 30 )
        except:
            messagebox.showerror ( "Value Error" , "There is A Value Error!!\nMath Domin Error!!" )

    btn = Button ( tl , text = "Log10(x)" , command = log )
    btn.place ( x = 200 , y = 120 , width = 80 , height = 80 )
    btn.config ( bg = "black" , fg = "white" )

    # ==================================LOG(X[,BASE])========================================
    def lg ( ):
        lb = ttk.Label ( tl )
        lb.place ( x = 200 , y = 80 )
        lb.config ( text = log ( int ( FN.get ( ) ) , int ( SN.get ( ) ) ) , width = 30 )

    btn = Button ( tl , text = "Logx(y)" , command = lg )
    btn.place ( x = 200 , y = 220 , width = 80 , height = 80 )

    # =================================RADIAN============================================
    def rad ( ):
        lb = ttk.Label ( tl )
        lb.place ( x = 200 , y = 80 )
        try:
            lb.config ( text = radians ( float ( FN.get ( ) ) ) , width = 30 )
        except:
            pass

    btn = Button ( tl , text = "To Radian(x)" , command = rad )
    btn.place ( x = 200 , y = 310 , width = 80 , height = 80 )

    # =================================DEGREE============================================
    def deg ( ):
        lb = ttk.Label ( tl )
        lb.place ( x = 200 , y = 80 )
        try:
            lb.config ( text = degrees ( float ( FN.get ( ) ) ) , width = 30 )
        except:
            pass

    btn = Button ( tl , text = "To Degree(x)" , command = deg )
    btn.place ( x = 200 , y = 400 , width = 80 , height = 80 )
    btn.config ( bg = "black" , fg = "white" )

    # =================================GAMMA(X)============================================
    def g ( ):
        lb = ttk.Label ( tl )
        lb.place ( x = 200 , y = 80 )
        try:
            lb.config ( text = gamma ( float ( FN.get ( ) ) ) , width = 30 )
        except:
            pass

    btn = Button ( tl , text = "Gamma(X)" , command = g )
    btn.place ( x = 290 , y = 120 , width = 80 , height = 80 )
    btn.config ( bg = "black" , fg = "white" )

    # =================================FLOOR(X)============================================
    def fl ( ):
        lb = ttk.Label ( tl )
        lb.place ( x = 200 , y = 80 )
        try:
            lb.config ( text = floor ( float ( FN.get ( ) ) ) , width = 30 )
        except:
            pass

    btn = Button ( tl , text = "[X] (Floor)" , command = fl )
    btn.place ( x = 290 , y = 220 , width = 80 , height = 80 )

    # =================================FABS(X)============================================
    def fb ( ):
        lb = ttk.Label ( tl )
        lb.place ( x = 200 , y = 80 )
        try:
            lb.config ( text = fabs ( float ( FN.get ( ) ) ) , width = 30 )
        except:
            pass

    btn = Button ( tl , text = "|X| (Fabs)" , command = fb )
    btn.place ( x = 290 , y = 310 , width = 80 , height = 80 )

    # =================================FMOD(X,Y)============================================
    def fm ( ):
        lb = ttk.Label ( tl )
        lb.place ( x = 200 , y = 80 )
        try:
            lb.config ( text = fmod ( float ( FN.get ( ) ) , float ( SN.get ( ) ) ) , width = 30 )
        except:
            pass

    btn = Button ( tl , text = "% (Fmod)" , command = fm )
    btn.place ( x = 290 , y = 400 , width = 80 , height = 80 )
    btn.config ( bg = "black" , fg = "white" )

    # =================================SIN(X)============================================
    def sn ( ):
        lb = ttk.Label ( tl )
        lb.place ( x = 200 , y = 80 )
        try:
            fn = radians ( float ( FN.get ( ) ) )
            lb.config ( text = sin ( fn ) , width = 30 )
        except:
            pass

    btn = Button ( tl , text = "Sin(X)" , command = sn )
    btn.place ( x = 380 , y = 120 , width = 80 , height = 80 )
    btn.config ( bg = "blue" , fg = "yellow" )

    # =================================ARC SIN(X)============================================
    def asn ( ):
        lb = ttk.Label ( tl )
        lb.place ( x = 200 , y = 80 )
        try:
            lb.config ( text = asin ( float ( FN.get ( ) ) ) , width = 30 )
        except:
            pass

    btn = Button ( tl , text = "aSin(X)\narc sin(x)" , command = asn )
    btn.place ( x = 470 , y = 120 , width = 80 , height = 80 )
    btn.config ( bg = "blue" , fg = "yellow" )

    # =================================COS(X)============================================
    def cs ( ):
        lb = ttk.Label ( tl )
        lb.place ( x = 200 , y = 80 )
        try:
            fn = radians ( float ( FN.get ( ) ) )
            lb.config ( text = cos ( fn ) , width = 30 )
        except:
            pass

    btn = Button ( tl , text = "Cos(X)" , command = cs )
    btn.place ( x = 380 , y = 220 , width = 80 , height = 80 )
    btn.config ( bg = "black" , fg = "white" )

    # =================================ARC COS(X)============================================
    def acs ( ):
        lb = ttk.Label ( tl )
        lb.place ( x = 200 , y = 80 )
        try:
            lb.config ( text = acos ( float ( FN.get ( ) ) ) , width = 30 )
        except:
            pass

    btn = Button ( tl , text = "aCos(X)\narc Cos(x)" , command = acs )
    btn.place ( x = 470 , y = 220 , width = 80 , height = 80 )
    btn.config ( bg = "blue" , fg = "yellow" )

    # =================================TAN(X)============================================
    def tn ( ):
        lb = ttk.Label ( tl )
        lb.place ( x = 200 , y = 80 )
        try:
            fn = radians ( float ( FN.get ( ) ) )
            lb.config ( text = tan ( fn ) , width = 30 )
        except:
            messagebox.showerror ( "Value Error!!!" , "Indefinable" )

    btn = Button ( tl , text = "Tan(X)" , command = tn )
    btn.place ( x = 380 , y = 310 , width = 80 , height = 80 )
    btn.config ( bg = "black" , fg = "white" )

    # =================================ARC TAN(X)============================================
    def atn ( ):
        lb = ttk.Label ( tl )
        lb.place ( x = 200 , y = 80 )
        try:
            lb.config ( text = atan ( float ( FN.get ( ) ) ) , width = 30 )
        except:
            pass

    btn = Button ( tl , text = "aTan(X)\narc Tan(x)" , command = atn )
    btn.place ( x = 470 , y = 310 , width = 80 , height = 80 )
    btn.config ( bg = "blue" , fg = "yellow" )

    # =================================FACTORIAL============================================
    def fact ( ):
        lb = ttk.Label ( tl )
        lb.place ( x = 200 , y = 80 )
        try:
            lb.config ( text = factorial ( float ( FN.get ( ) ) ) , width = 30 )
        except:
            pass

    btn = Button ( tl , text = "X! (Factorial)" , command = fact )
    btn.place ( x = 380 , y = 400 , width = 80 , height = 80 )
    btn.config ( bg = "blue" , fg = "yellow" )

    # =================================HYPOT(X,Y)============================================
    def hp ( ):
        lb = ttk.Label ( tl )
        lb.place ( x = 200 , y = 80 )
        try:
            lb.config ( text = hypot ( float ( FN.get ( ) ) , float ( SN.get ( ) ) ) , width = 30 )
        except:
            pass

    btn = Button ( tl , text = "Hypot(x,y)\n√(x**2 + y**2)" , command = hp )
    btn.place ( x = 470 , y = 400 , width = 80 , height = 80 )
    btn.config ( bg = "blue" , fg = "yellow" )


btn1 = ttk.Button ( win , text = "Calculator" , command = calculator )
btn1.place ( x = 250 , y = 250 )
btn1.config ( width = 20 )
ax1 = PhotoImage ( file = "math.png" )
btn1.config ( image = ax1 , compound = "top" )


# =========================================================================================
# =========================================================================================

def shape ( ):
    tl = Toplevel ( win )
    tl.geometry ( "500x500" )
    tl.title ( "Shape" )
    tl.config ( bg = "light green" )
    btn = ttk.Button ( tl , text = "exit" , command = tl.destroy )
    btn.place ( x = 250 , y = 450 )
    lbs = ttk.Label ( tl , text = "S" )
    lbs.place ( x = 210 , y = 100 )
    lbs.config ( font = ("impact" , 130) , background = "light green" )

    # ===================================================SQUARE=====================================
    def square ( ):
        tl = Toplevel ( win )
        tl.geometry ( "500x500" )
        tl.title ( "Square" )
        tl.config ( bg = "light blue" )
        btn = ttk.Button ( tl , text = "exit" , command = tl.destroy )
        btn.place ( x = 250 , y = 450 )
        lb = Label ( tl , text = "Result: " )
        lb.place ( x = 50 , y = 300 )
        menubar = Menu ( tl )
        tl.config ( menu = menubar )
        aboutmenu = Menu ( menubar , tearoff = 0 )

        def about ( ):
            tl1 = Toplevel ( tl )
            tl1.title ( "About Square" )
            lb = ttk.Label ( tl1 , text = "Square" , font = ("arial" , 18 , "bold") ).place ( x = 30 , y = 40 )
            lb1 = ttk.Label ( tl1 , text = "1 : Circumference = X * 4" ).place ( x = 30 , y = 80 )
            lb2 = ttk.Label ( tl1 , text = "2 : Area = X * X  OR  X ** 2" ).place ( x = 30 , y = 110 )
            lb3 = ttk.Label ( tl1 , text = "3 : Volume = X * X * X  OR  X ** 3" ).place ( x = 30 , y = 140 )

        aboutmenu.add_command ( label = "About" , command = about )
        menubar.add_cascade ( label = "About" , menu = aboutmenu )
        lb1 = ttk.Label ( tl , text = "Side: " )
        lb1.place ( x = 130 , y = 20 )
        S = ttk.Entry ( tl )
        S.place ( x = 200 , y = 20 )

        # CIRCUMFERENCE
        def circum ( ):
            lb = ttk.Label ( tl )
            lb.place ( x = 100 , y = 300 )
            lb.config ( text = float ( S.get ( ) ) * 4 , width = 30 )

        btn = ttk.Button ( tl , text = "Circumference" , command = circum )
        btn.place ( x = 20 , y = 200 )

        # AREA
        def area ( ):
            lb = ttk.Label ( tl )
            lb.place ( x = 100 , y = 300 )
            lb.config ( text = float ( S.get ( ) ) ** 2 , width = 30 )

        btn = ttk.Button ( tl , text = "Area" , command = area )
        btn.place ( x = 150 , y = 200 )

        # VOLUME
        def volume ( ):
            lb = ttk.Label ( tl )
            lb.place ( x = 100 , y = 300 )
            lb.config ( text = float ( S.get ( ) ) ** 3 , width = 30 )

        btn = ttk.Button ( tl , text = "Volume" , command = volume )
        btn.place ( x = 280 , y = 200 )

    btns = ttk.Button ( tl , text = "Square" , command = square )
    btns.place ( x = 220 , y = 50 )

    # ==================================================RECTANGULAR==================================
    def rect ( ):
        tl = Toplevel ( win )
        tl.geometry ( "500x500" )
        tl.title ( "Rectangular" )
        tl.config ( bg = "light blue" )
        btn = ttk.Button ( tl , text = "exit" , command = tl.destroy )
        btn.place ( x = 250 , y = 450 )
        lb = Label ( tl , text = "Result: " )
        lb.place ( x = 50 , y = 300 )
        menubar = Menu ( tl )
        tl.config ( menu = menubar )
        aboutmenu = Menu ( menubar , tearoff = 0 )

        def about ( ):
            tl1 = Toplevel ( tl )
            tl1.title ( "About Rectangular" )
            lb = ttk.Label ( tl1 , text = "Rectangular" , font = ("arial" , 18 , "bold") ).place ( x = 30 , y = 40 )
            lb1 = ttk.Label ( tl1 , text = "1 : Circumference = (X + Y) * 2" ).place ( x = 30 , y = 80 )
            lb2 = ttk.Label ( tl1 , text = "2 : Area = X * Y" ).place ( x = 30 , y = 110 )
            lb3 = ttk.Label ( tl1 , text = "3 : Volume = X * Y * H" ).place ( x = 30 , y = 140 )

        aboutmenu.add_command ( label = "About" , command = about )
        menubar.add_cascade ( label = "About" , menu = aboutmenu )
        lb1 = ttk.Label ( tl , text = "First Side: " )
        lb1.place ( x = 130 , y = 20 )
        FS = ttk.Entry ( tl )
        FS.place ( x = 200 , y = 20 )
        lb2 = ttk.Label ( tl , text = "Second Side: " )
        lb2.place ( x = 112 , y = 50 )
        SS = ttk.Entry ( tl )
        SS.place ( x = 200 , y = 50 )
        lb3 = ttk.Label ( tl , text = "height: " )
        lb3.place ( x = 130 , y = 80 )
        H = ttk.Entry ( tl )
        H.place ( x = 200 , y = 80 )

        # CIRCUMFERENCE
        def circum ( ):
            lb = ttk.Label ( tl )
            lb.place ( x = 100 , y = 300 )
            lb.config ( text = (float ( FS.get ( ) ) + float ( SS.get ( ) )) * 2 , width = 30 )

        btn = ttk.Button ( tl , text = "Circumference" , command = circum )
        btn.place ( x = 20 , y = 200 )

        # AREA
        def area ( ):
            lb = ttk.Label ( tl )
            lb.place ( x = 100 , y = 300 )
            lb.config ( text = float ( FS.get ( ) ) * float ( SS.get ( ) ) , width = 30 )

        btn = ttk.Button ( tl , text = "Area" , command = area )
        btn.place ( x = 150 , y = 200 )

        # VOLUME
        def volume ( ):
            lb = ttk.Label ( tl )
            lb.place ( x = 100 , y = 300 )
            lb.config ( text = float ( FS.get ( ) ) * float ( SS.get ( ) ) * float ( H.get ( ) ) , width = 30 )

        btn = ttk.Button ( tl , text = "Volume" , command = volume )
        btn.place ( x = 280 , y = 200 )

    btns = ttk.Button ( tl , text = "Rectangular" , command = rect )
    btns.place ( x = 170 , y = 100 )

    # ==============================================TRIANGULAR===================================
    def trian ( ):
        tl = Toplevel ( win )
        tl.geometry ( "500x500" )
        tl.title ( "Triangular" )
        tl.config ( bg = "light blue" )
        btn = ttk.Button ( tl , text = "exit" , command = tl.destroy )
        btn.place ( x = 250 , y = 450 )
        lb1 = ttk.Label ( tl , text = "First Side: " )
        lb1.place ( x = 130 , y = 20 )
        lb = Label ( tl , text = "Result: " )
        lb.place ( x = 50 , y = 300 )
        menubar = Menu ( tl )
        tl.config ( menu = menubar )
        aboutmenu = Menu ( menubar , tearoff = 0 )

        def about ( ):
            tl1 = Toplevel ( tl )
            tl1.title ( "About Triangular" )
            lb = ttk.Label ( tl1 , text = "Triangular" , font = ("arial" , 18 , "bold") ).place ( x = 30 , y = 40 )
            lb1 = ttk.Label ( tl1 , text = "1 : Circumference = X + Y + Z" ).place ( x = 30 , y = 80 )
            lb2 = ttk.Label ( tl1 , text = "2 : Area = ( X * Y ) / 2" ).place ( x = 30 , y = 110 )

        aboutmenu.add_command ( label = "About" , command = about )
        menubar.add_cascade ( label = "About" , menu = aboutmenu )
        FS = ttk.Entry ( tl )
        FS.place ( x = 200 , y = 20 )
        lb2 = ttk.Label ( tl , text = "Second Side: " )
        lb2.place ( x = 112 , y = 50 )
        SS = ttk.Entry ( tl )
        SS.place ( x = 200 , y = 50 )
        lb3 = ttk.Label ( tl , text = "Third Side(G): " )
        lb3.place ( x = 120 , y = 80 )
        TS = ttk.Entry ( tl )
        TS.place ( x = 200 , y = 80 )
        lb4 = ttk.Label ( tl , text = "height: " )
        lb4.place ( x = 130 , y = 110 )
        H = ttk.Entry ( tl )
        H.place ( x = 200 , y = 110 )

        # CIRCUMFERENCE
        def circum ( ):
            lb = ttk.Label ( tl )
            lb.place ( x = 100 , y = 300 )
            lb.config ( text = (float ( FS.get ( ) ) + float ( SS.get ( ) )) + float ( TS.get ( ) ) , width = 30 )

        btn = ttk.Button ( tl , text = "Circumference" , command = circum )
        btn.place ( x = 20 , y = 200 )

        # AREA
        def area ( ):
            lb = ttk.Label ( tl )
            lb.place ( x = 100 , y = 300 )
            lb.config ( text = (float ( TS.get ( ) ) * int ( H.get ( ) )) / 2 , width = 30 )

        btn = ttk.Button ( tl , text = "Area" , command = area )
        btn.place ( x = 150 , y = 200 )

    btns = ttk.Button ( tl , text = "Triangular" , command = trian )
    btns.place ( x = 270 , y = 100 )

    # =======================================================CIRCLE======================================
    def circle ( ):
        tl = Toplevel ( win )
        tl.geometry ( "500x500" )
        tl.title ( "Circle" )
        tl.config ( bg = "light blue" )
        btn = ttk.Button ( tl , text = "exit" , command = tl.destroy )
        btn.place ( x = 250 , y = 450 )
        lb = Label ( tl , text = "Result: " )
        lb.place ( x = 50 , y = 300 )
        menubar = Menu ( tl )
        tl.config ( menu = menubar )
        aboutmenu = Menu ( menubar , tearoff = 0 )

        def about ( ):
            tl1 = Toplevel ( tl )
            tl1.title ( "About Circle" )
            lb = ttk.Label ( tl1 , text = "Circle" , font = ("arial" , 18 , "bold") ).place ( x = 30 , y = 40 )
            lb1 = ttk.Label ( tl1 , text = "1 : Circumference = R * PI * 2" ).place ( x = 30 , y = 80 )
            lb2 = ttk.Label ( tl1 , text = "2 : Area = ( R ** 2 ) * PI" ).place ( x = 30 , y = 110 )

        aboutmenu.add_command ( label = "About" , command = about )
        menubar.add_cascade ( label = "About" , menu = aboutmenu )
        lb1 = ttk.Label ( tl , text = "Radius: " )
        lb1.place ( x = 130 , y = 20 )
        R = ttk.Entry ( tl )
        lb = Label ( tl , text = "Result: " )
        lb.place ( x = 50 , y = 300 )
        R.place ( x = 200 , y = 20 )
        PI = 3.14

        # CIRCUMFERENCE
        def circum ( ):
            lb = ttk.Label ( tl )
            lb.place ( x = 100 , y = 300 )
            lb.config ( text = float ( R.get ( ) ) * PI * 2 , width = 30 )

        btn = ttk.Button ( tl , text = "Circumference" , command = circum )
        btn.place ( x = 20 , y = 200 )

        # AREA
        def area ( ):
            lb = ttk.Label ( tl )
            lb.place ( x = 100 , y = 300 )
            lb.config ( text = (float ( R.get ( ) ) ** 2) * PI , width = 30 )

        btn = ttk.Button ( tl , text = "Area" , command = area )
        btn.place ( x = 150 , y = 200 )

    btns = ttk.Button ( tl , text = "Circle" , command = circle )
    btns.place ( x = 130 , y = 150 )

    # ===================================================SPHERE=======================================
    def sphere ( ):
        tl = Toplevel ( win )
        tl.geometry ( "500x500" )
        tl.title ( "Sphere" )
        tl.config ( bg = "light blue" )
        btn = ttk.Button ( tl , text = "exit" , command = tl.destroy )
        btn.place ( x = 250 , y = 450 )
        lb = Label ( tl , text = "Result: " )
        lb.place ( x = 50 , y = 300 )
        menubar = Menu ( tl )
        tl.config ( menu = menubar )
        aboutmenu = Menu ( menubar , tearoff = 0 )

        def about ( ):
            tl1 = Toplevel ( tl )
            tl1.title ( "About Sphere" )
            lb = ttk.Label ( tl1 , text = "Sphere" , font = ("arial" , 18 , "bold") ).place ( x = 30 , y = 40 )
            lb1 = ttk.Label ( tl1 , text = "1 : Area = ( R ** 2 ) * PI * 4" ).place ( x = 30 , y = 80 )
            lb2 = ttk.Label ( tl1 , text = "2 : Volume = ( R ** 3 ) * PI * 1.3333" ).place ( x = 30 , y = 110 )

        aboutmenu.add_command ( label = "About" , command = about )
        menubar.add_cascade ( label = "About" , menu = aboutmenu )
        lb1 = ttk.Label ( tl , text = "Radius: " )
        lb1.place ( x = 130 , y = 20 )
        R = ttk.Entry ( tl )
        R.place ( x = 200 , y = 20 )
        PI = 3.14

        # AREA
        def area ( ):
            lb = ttk.Label ( tl )
            lb.place ( x = 100 , y = 300 )
            lb.config ( text = (float ( R.get ( ) ) ** 2) * PI * 4 , width = 30 )

        btn = ttk.Button ( tl , text = "Area" , command = area )
        btn.place ( x = 150 , y = 200 )

        # VOLUME
        def volume ( ):
            lb = ttk.Label ( tl )
            lb.place ( x = 100 , y = 300 )
            lb.config ( text = (float ( R.get ( ) ) ** 3) * PI * 1.333 , width = 30 )

        btn = ttk.Button ( tl , text = "Volume" , command = volume )
        btn.place ( x = 250 , y = 200 )

    btns = ttk.Button ( tl , text = "Sphere" , command = sphere )
    btns.place ( x = 310 , y = 150 )

    # ================================================LOZENGE==========================================
    def lozenge ( ):
        tl = Toplevel ( win )
        tl.geometry ( "500x500" )
        tl.title ( "Lozenge" )
        tl.config ( bg = "light blue" )
        btn = ttk.Button ( tl , text = "exit" , command = tl.destroy )
        btn.place ( x = 250 , y = 450 )
        lb = Label ( tl , text = "Result: " )
        lb.place ( x = 50 , y = 300 )
        menubar = Menu ( tl )
        tl.config ( menu = menubar )
        aboutmenu = Menu ( menubar , tearoff = 0 )

        def about ( ):
            tl1 = Toplevel ( tl )
            tl1.title ( "About Lozenge" )
            lb = ttk.Label ( tl1 , text = "Lozenge" , font = ("arial" , 18 , "bold") ).place ( x = 30 , y = 40 )
            lb1 = ttk.Label ( tl1 , text = "1 : Circumference = X * 4" ).place ( x = 30 , y = 80 )
            lb2 = ttk.Label ( tl1 , text = "2 : Area = ( Z * Y ) / 2" ).place ( x = 30 , y = 110 )

        aboutmenu.add_command ( label = "About" , command = about )
        menubar.add_cascade ( label = "About" , menu = aboutmenu )
        lb1 = ttk.Label ( tl , text = "Side: " )
        lb1.place ( x = 130 , y = 20 )
        S = ttk.Entry ( tl )
        S.place ( x = 200 , y = 20 )
        lb2 = ttk.Label ( tl , text = "little Diagonal: " )
        lb2.place ( x = 110 , y = 50 )
        LD = ttk.Entry ( tl )
        LD.place ( x = 200 , y = 50 )
        lb3 = ttk.Label ( tl , text = "Great Diagonal: " )
        lb3.place ( x = 105 , y = 80 )
        GD = ttk.Entry ( tl )
        GD.place ( x = 200 , y = 80 )

        # CIRCUMFERENCE
        def circum ( ):
            lb = ttk.Label ( tl )
            lb.place ( x = 100 , y = 300 )
            lb.config ( text = float ( S.get ( ) ) * 4 , width = 30 )

        btn = ttk.Button ( tl , text = "Circumference" , command = circum )
        btn.place ( x = 20 , y = 200 )

        # AREA
        def area ( ):
            lb = ttk.Label ( tl )
            lb.place ( x = 100 , y = 300 )
            lb.config ( text = (float ( GD.get ( ) ) * float ( LD.get ( ) )) / 2 , width = 30 )

        btn = ttk.Button ( tl , text = "Area" , command = area )
        btn.place ( x = 150 , y = 200 )

    btns = ttk.Button ( tl , text = "Lozenge" , command = lozenge )
    btns.place ( x = 90 , y = 200 )

    # ==================================================PARALLELOGRAM===============================
    def parallelogran ( ):
        tl = Toplevel ( win )
        tl.geometry ( "500x500" )
        tl.title ( "Parallelogran" )
        tl.config ( bg = "light blue" )
        btn = ttk.Button ( tl , text = "exit" , command = tl.destroy )
        btn.place ( x = 250 , y = 450 )
        lb = Label ( tl , text = "Result: " )
        lb.place ( x = 50 , y = 300 )
        menubar = Menu ( tl )
        tl.config ( menu = menubar )
        aboutmenu = Menu ( menubar , tearoff = 0 )

        def about ( ):
            tl1 = Toplevel ( tl )
            tl1.title ( "About Parallelogran" )
            lb = ttk.Label ( tl1 , text = "Parallelogran" , font = ("arial" , 18 , "bold") ).place ( x = 30 , y = 40 )
            lb1 = ttk.Label ( tl1 , text = "1 : Circumference = (X + Y) * 2" ).place ( x = 30 , y = 80 )
            lb2 = ttk.Label ( tl1 , text = "2 : Area = X * H" ).place ( x = 30 , y = 110 )

        aboutmenu.add_command ( label = "About" , command = about )
        menubar.add_cascade ( label = "About" , menu = aboutmenu )
        lb1 = ttk.Label ( tl , text = "First Side(G): " )
        lb1.place ( x = 130 , y = 20 )
        FS = ttk.Entry ( tl )
        FS.place ( x = 200 , y = 20 )
        lb1 = ttk.Label ( tl , text = "Second Side: " )
        lb1.place ( x = 130 , y = 50 )
        SS = ttk.Entry ( tl )
        SS.place ( x = 200 , y = 50 )
        lb1 = ttk.Label ( tl , text = "Height: " )
        lb1.place ( x = 130 , y = 80 )
        H = ttk.Entry ( tl )
        H.place ( x = 200 , y = 80 )

        # CIRCUMFERENCE
        def circum ( ):
            lb = ttk.Label ( tl )
            lb.place ( x = 100 , y = 300 )
            lb.config ( text = (float ( FS.get ( ) ) + float ( SS.get ( ) )) * 2 , width = 30 )

        btn = ttk.Button ( tl , text = "Circumference" , command = circum )
        btn.place ( x = 20 , y = 200 )

        # AREA
        def area ( ):
            lb = ttk.Label ( tl )
            lb.place ( x = 100 , y = 300 )
            lb.config ( text = float ( FS.get ( ) ) * float ( H.get ( ) ) , width = 30 )

        btn = ttk.Button ( tl , text = "Area" , command = area )
        btn.place ( x = 150 , y = 200 )

    btns = ttk.Button ( tl , text = "Parallelogran" , command = parallelogran )
    btns.place ( x = 350 , y = 200 )

    # ==================================================ELLIPSE======================================
    def ellipse ( ):
        tl = Toplevel ( win )
        tl.geometry ( "500x500" )
        tl.title ( "Ellipse" )
        tl.config ( bg = "light blue" )
        btn = ttk.Button ( tl , text = "exit" , command = tl.destroy )
        btn.place ( x = 250 , y = 450 )
        lb = Label ( tl , text = "Result: " )
        lb.place ( x = 50 , y = 300 )
        menubar = Menu ( tl )
        tl.config ( menu = menubar )
        aboutmenu = Menu ( menubar , tearoff = 0 )

        def about ( ):
            tl1 = Toplevel ( tl )
            tl1.title ( "About Ellipse" )
            lb = ttk.Label ( tl1 , text = "Ellipse" , font = ("arial" , 18 , "bold") ).place ( x = 30 , y = 40 )
            lb2 = ttk.Label ( tl1 , text = "1 : Area = ( X * Y ) * PI" ).place ( x = 30 , y = 110 )

        aboutmenu.add_command ( label = "About" , command = about )
        menubar.add_cascade ( label = "About" , menu = aboutmenu )
        lb1 = ttk.Label ( tl , text = "First Diagonal: " )
        lb1.place ( x = 120 , y = 20 )
        FD = ttk.Entry ( tl )
        FD.place ( x = 200 , y = 20 )
        lb1 = ttk.Label ( tl , text = "Second Diagonal: " )
        lb1.place ( x = 105 , y = 50 )
        SD = ttk.Entry ( tl )
        SD.place ( x = 200 , y = 50 )
        PI = 3.14

        # AREA
        def area ( ):
            lb = ttk.Label ( tl )
            lb.place ( x = 100 , y = 300 )
            lb.config ( text = ((float ( FD.get ( ) ) / 2) * (float ( SD.get ( ) )) / 2) * PI , width = 30 )

        btn = ttk.Button ( tl , text = "Area" , command = area )
        btn.place ( x = 150 , y = 200 )

    btns = ttk.Button ( tl , text = "Ellipse" , command = ellipse )
    btns.place ( x = 50 , y = 250 )

    # =================================================TRAPEZE==========================================
    def trapeze ( ):
        tl = Toplevel ( win )
        tl.geometry ( "500x500" )
        tl.title ( "Trapeze" )
        tl.config ( bg = "light blue" )
        btn = ttk.Button ( tl , text = "exit" , command = tl.destroy )
        btn.place ( x = 250 , y = 450 )
        lb = Label ( tl , text = "Result: " )
        lb.place ( x = 50 , y = 300 )
        menubar = Menu ( tl )
        tl.config ( menu = menubar )
        aboutmenu = Menu ( menubar , tearoff = 0 )

        def about ( ):
            tl1 = Toplevel ( tl )
            tl1.title ( "About Trapeze" )
            lb = ttk.Label ( tl1 , text = "Trapeze" , font = ("arial" , 18 , "bold") ).place ( x = 30 , y = 40 )
            lb1 = ttk.Label ( tl1 , text = "1 : Circumference = X + Y + Z + W" ).place ( x = 30 , y = 80 )
            lb2 = ttk.Label ( tl1 , text = "2 : Area = ( Z + W ) * ( H / 2 )" ).place ( x = 30 , y = 110 )

        aboutmenu.add_command ( label = "About" , command = about )
        menubar.add_cascade ( label = "About" , menu = aboutmenu )
        lb1 = ttk.Label ( tl , text = "First Side(BG): " )
        lb1.place ( x = 110 , y = 20 )
        FS = ttk.Entry ( tl )
        FS.place ( x = 200 , y = 20 )
        lb1 = ttk.Label ( tl , text = "Second Side(LG): " )
        lb1.place ( x = 100 , y = 50 )
        SS = ttk.Entry ( tl )
        SS.place ( x = 200 , y = 50 )
        lb1 = ttk.Label ( tl , text = "Third Side: " )
        lb1.place ( x = 130 , y = 80 )
        TS = ttk.Entry ( tl )
        TS.place ( x = 200 , y = 80 )
        lb1 = ttk.Label ( tl , text = "Forth Side: " )
        lb1.place ( x = 130 , y = 110 )
        FOS = ttk.Entry ( tl )
        FOS.place ( x = 200 , y = 110 )
        lb1 = ttk.Label ( tl , text = "Height: " )
        lb1.place ( x = 130 , y = 140 )
        H = ttk.Entry ( tl )
        H.place ( x = 200 , y = 140 )

        # CIRCUMFERENCE
        def circum ( ):
            lb = ttk.Label ( tl )
            lb.place ( x = 100 , y = 300 )
            lb.config (
                text = float ( FS.get ( ) ) + float ( SS.get ( ) ) + float ( TS.get ( ) ) + float ( FOS.get ( ) ) ,
                width = 30 )

        btn = ttk.Button ( tl , text = "Circumference" , command = circum )
        btn.place ( x = 20 , y = 200 )

        # AREA
        def area ( ):
            lb = ttk.Label ( tl )
            lb.place ( x = 100 , y = 300 )
            lb.config ( text = (float ( FS.get ( ) ) + float ( SS.get ( ) )) * (float ( H.get ( ) ) / 2) , width = 30 )

        btn = ttk.Button ( tl , text = "Area" , command = area )
        btn.place ( x = 150 , y = 200 )

    btns = ttk.Button ( tl , text = "Trapeze" , command = trapeze )
    btns.place ( x = 390 , y = 250 )
    menubar = Menu ( tl )
    tl.config ( menu = menubar )
    filemenu = Menu ( menubar , tearoff = 0 )
    filemenu.add_command ( label = "Square" , command = square )
    filemenu.add_command ( label = "Rectangular" , command = rect )
    filemenu.add_command ( label = "Triangularr" , command = trian )
    filemenu.add_command ( label = "Circle" , command = circle )
    filemenu.add_command ( label = "Sphere" , command = sphere )
    filemenu.add_command ( label = "Lozenge" , command = lozenge )
    filemenu.add_command ( label = "Parallelogran" , command = parallelogran )
    filemenu.add_command ( label = "Ellipse" , command = ellipse )
    filemenu.add_command ( label = "Trapeze" , command = trapeze )
    # filemenu.add_command(label="Cylinder", command=cylinder)
    filemenu.add_separator ( )
    filemenu.add_command ( label = "Quit" , command = tl.destroy )
    menubar.add_cascade ( label = "File" , menu = filemenu )


btn2 = ttk.Button ( win , text = "Shapes" , command = shape )
btn2.place ( x = 70 , y = 250 )
btn2.config ( width = 20 )
ax = PhotoImage ( file = "shape.png" )
btn2.config ( image = ax , compound = "top" )

menubar = Menu ( win )
win.config ( menu = menubar )
filemenu = Menu ( menubar , tearoff = 0 )
filemenu.add_command ( label = "Calculator" , command = calculator )
filemenu.add_command ( label = "Shape" , command = shape )
filemenu.add_separator ( )
filemenu.add_command ( label = "Quit" , command = win.destroy )
menubar.add_cascade ( label = "File" , menu = filemenu )

# ======================================================================================
# ======================================================================================


win.mainloop ( )
