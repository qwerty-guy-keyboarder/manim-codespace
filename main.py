from manim import *


class TanLine(Scene):
    def construct(self):


        ################# SETUP ########################

        #Create Title
        title = MathTex(r"\text{Consider the curve   }y=", r"\psi(x)=\frac{3}{4}x-3\sqrt{x}-3.", r"\text{  Find the line tangent to this curve when }", r"x=1", r".").scale(0.6).to_edge(UP)        
        #Set the function blue and the x value green
        title[1].set_color(BLUE)
        title[3].set_color(GREEN)


        #Set up the lowest and greatest x values of our region as well as where the tick marks on the axis go
        xmin = 0
        xmax = 5
        xtick = 2

        #Set up the lowest and greatest y values of our region as well as where the tick marks on the axis go
        ymin = -8
        ymax = 2
        ytick = 4


        #Creates an cartesian plane and moves it to the left side of the screen.
        axes = Axes(x_range=[xmin, xmax, xtick], y_range=[ymin, ymax, ytick], x_length=5.5, y_length=5.5, ).shift(LEFT*3.5)
        numberplane = NumberPlane(x_range=[xmin, xmax, xtick], y_range=[ymin, ymax, ytick],   x_length=5.5, y_length=5.5,).shift(LEFT*3.5)
        

        #Plot function f(x) = (3/4)x-3x^(1/2)-1 on the coordinate axes    
        plot1 = axes.plot(lambda x: 3/4*x-3*(x)**(1/2)-1,  x_range=[xmin, xmax, 0.01], color=YELLOW)
        
        #Create a point and a label by the point
        p0 = Dot(axes.c2p(1,-13/4), color=BLUE)
        label0 = MathTex(r"(1,-13/4)", color=BLUE).scale(0.4).next_to(p0, UP+RIGHT)

        #Create tanline
        tanline = axes.plot(lambda x: -3/4*(x-1)-13/4,  x_range=[xmin, xmax, 0.01], color=GREEN)
        #Make tanline dashed
        tanline=DashedVMobject(tanline)


        


        #Creates empty storage arrays, eq signs, left hand sides and right hand sides
        eq=[0,0, 0,0,0,0,0]
        lhs=[0,0, 0,0,0,0,0]
        rhs=[0,0, 0,0,0,0,0]




        #Creates an = sign shifted to the up right from center, and 6 more equal signs aligned below it.
        eq[0] = MathTex(r"=").scale(0.6).shift(UP*2+RIGHT*1)
        for i in range(6):
            eq[i+1] = MathTex(r"=").scale(0.6).next_to(eq[i], DOWN*3.5)


        #Creates the first left hand side, and right hand side
        lhs[0] = MathTex(r"\psi(x)", color=BLUE).scale(0.6).next_to(eq[0], LEFT)
        rhs[0] = MathTex(r"\frac{3}{4}x-3\sqrt{x}-3",).scale(0.6).next_to(eq[0], RIGHT)
        #Creates item the righthandside will turn into
        rhs0a = MathTex(r"\frac{3}{4}x-3x^{1/2}-3",).scale(0.6).next_to(eq[0], RIGHT)

        #Creates the second lefthandside, making the "1" of the psi(1) it's own entry in the arrray
        lhs[1] = MathTex(r"\psi(", r"1", r")", ).scale(0.6).next_to(eq[1], LEFT)
        #Set the 1 to be green
        lhs[1][1].set_color(GREEN)
        #Creates the second righthandside and sets the second entry Orange
        rhs[1] = MathTex(r"\frac{3}{4}(1)-3\sqrt{1}-3",r"=-\frac{13}{4}").scale(0.6).next_to(eq[1], RIGHT)
        rhs[1][1].set_color(ORANGE)

        #Creates the third lefthandside, righthandside, and a transformation of the third lefthandside
        lhs[2] = MathTex(r"\psi'(x)", color=PURPLE).scale(0.6).next_to(eq[2], LEFT)
        rhs[2] = MathTex(r"\frac{3}{4} - \frac{3}{2}x^{-1/2}", ).scale(0.6).next_to(eq[2], RIGHT)
        rhs2a = MathTex(r"\frac{3}{4} - \frac{3}{2\sqrt{x}}", ).scale(0.6).next_to(eq[2], RIGHT)

        
        #Creates a fourth lefthandside, righthandside, and sets the last element of the third righthandside Purple
        lhs[3] = MathTex(r"\psi'(1)", color=PURPLE).scale(0.6).next_to(eq[3], LEFT)
        rhs[3] = MathTex(r"\frac{3}{4} - \frac{3}{2\sqrt{1}}", r"=", r"-\frac{3}{4}" ).scale(0.6).next_to(eq[3], RIGHT)
        rhs[3][2].set_color(PURPLE)

        #Creates the fifth lefthandside and righthandside, setting multiple pieces of the rhs various colors to match their corresponding colors above
        lhs[4] = MathTex(r"y", ).scale(0.6).next_to(eq[4], LEFT)
        rhs[4] = MathTex(r"-\frac{3}{4}", r"(x-", r"1", r")", r"-\frac{13}{4}" ).scale(0.6).next_to(eq[4], RIGHT)
        rhs[4][0].set_color(PURPLE)
        rhs[4][2].set_color(GREEN)
        rhs[4][4].set_color(ORANGE)

        #Creates the sixth righthandside
        rhs[5] = MathTex(r"-\frac{3}{4}x - \frac{5}{2}", ).scale(0.6).next_to(eq[5], RIGHT)

        

        
        #################### ANIMATION ###########################

        #Creates the title, and coordinate plane
        self.play( Write(title), Create(axes), Create(numberplane), )# Create(fun))
        #Pause for 3 seconds
        self.wait(3)
        #Draw the function
        self.play(Create(plot1))
        self.wait(5)

        #Write first equation
        self.play(Write(lhs[0]))
        self.wait(2)
        self.play(Write(eq[0]), Write(rhs[0]))
        self.wait(5)

        #Write second equation
        self.play(Write(lhs[1]))
        self.wait(2)
        self.play(Write(eq[1]), Write(rhs[1]))
        self.wait(2)

        #Creates point and label on plane
        self.play(Create(p0), Create(label0))
        self.wait(5)


        #Create third equation
        self.play(Write(lhs[2]))
        self.wait(2)
        #Rewrite rhs of first equation in terms of power functions
        self.play(Transform(rhs[0], rhs0a))
        self.wait(3)
        self.play(Write(eq[2]), Write(rhs[2]))
        self.wait(5)
        #Rewrites psi' using quotients and square roots
        self.play(Transform(rhs[2], rhs2a))

        #Write Fourth Equation
        self.play(Write(lhs[3]))
        self.wait(2)
        self.play(Write(eq[3]), Write(rhs[3][0]))
        self.wait(3)
        self.play(Write(rhs[3][1]), Write(rhs[3][2]))
        self.wait(5)

        #Write fifth equation
        self.play(Write(lhs[4]))
        self.wait(2)
        self.play(Write(eq[4]), Write(rhs[4]))
        self.wait(5)

        #Write last line
        self.play(Write(eq[5]), Write(rhs[5]), Create(tanline))
        

        self.wait(10)   



class SinChange(Scene):
    def construct(self):


        ################# SETUP ########################

        #Create Title
        title = MathTex(r"\text{Consider the curve   }y=", r"a",r"\sin(", r"b", r"x)+", r"c", r".").scale(0.6).to_edge(UP)        
        #Set a blue, b green and c red
        title[1].set_color(BLUE)
        title[3].set_color(GREEN)
        title[5].set_color(RED)


        
        #Set up the lowest and greatest x values of our region as well as where the tick marks on the axis go
        xmin = -5
        xmax = 5
        xtick = 2

        #Set up the lowest and greatest y values of our region as well as where the tick marks on the axis go
        ymin = -5
        ymax = 5
        ytick = 2


        #Creates an cartesian plane and moves it to the left side of the screen.
        axes = Axes(x_range=[xmin, xmax, xtick], y_range=[ymin, ymax, ytick], x_length=5.5, y_length=5.5, ).shift(LEFT*3.5)
        numberplane = NumberPlane(x_range=[xmin, xmax, xtick], y_range=[ymin, ymax, ytick],   x_length=5.5, y_length=5.5,).shift(LEFT*3.5)
        

        #Plot function f(x) = sin(x) using numpy on the coordinate axes    
        plot1 = axes.plot(lambda x: np.sin(x),  x_range=[xmin, xmax, 0.01], color=YELLOW)
        
        # Creates trackers for a, b, c

        tracka=ValueTracker(1)
        trackb=ValueTracker(1)
        trackc=ValueTracker(0)


        #Creates an updater for plot1 using the tracker values
        def updateplot1(mob):
            mob.become(
                axes.plot(lambda x: tracka.get_value()*np.sin(trackb.get_value()*x)+trackc.get_value(), 
                x_range=[-5, 5], 
                use_smoothing=True,
                color=YELLOW)
                )

        plot1.add_updater(updateplot1)

        


        #Creates empty storage arrays, eq signs, left hand sides and right hand sides
        eq=[0,0, 0,0,0,0,0]
        lhs=[0,0, 0,0,0,0,0]
        rhs=[0,0, 0,0,0,0,0]

        #Creates a vector for the a, b, c values
        a=[1,2, 2,  2,  -1/3,0,0]
        b=[1,1, 1/2,1/2,-2,0,0]
        c=[0,0, 0,  -3, 2,0,0]




        #Creates an = sign shifted to the up right from center, and 6 more equal signs aligned below it.
        eq[0] = MathTex(r"=").scale(0.6).shift(UP*2+RIGHT*1)
        for i in range(6):
            eq[i+1] = MathTex(r"=").scale(0.6).next_to(eq[i], DOWN*3.5)


        #Creates the first left hand side, and right hand side
        lhs[0] = MathTex(r"y", ).scale(0.6).next_to(eq[0], LEFT)
        rhs[0] = MathTex(r"1",r"\cdot\sin(", r"1", r"\cdot x)+", r"0").scale(0.6).next_to(eq[0], RIGHT)
        #Set the RHS Colors
        rhs[0][0].set_color(BLUE)
        rhs[0][2].set_color(GREEN)
        rhs[0][4].set_color(RED)

        #Creates the second left hand side, and right hand side
        lhs[1] = MathTex(r"y", ).scale(0.6).next_to(eq[1], LEFT)
        rhs[1] = MathTex(r"2",r"\cdot\sin(", r"1", r"\cdot x)+", r"0").scale(0.6).next_to(eq[1], RIGHT)
        #Set the RHS Colors
        rhs[1][0].set_color(BLUE)
        rhs[1][2].set_color(GREEN)
        rhs[1][4].set_color(RED)

        #Creates the third left hand side, and right hand side
        lhs[2] = MathTex(r"y", ).scale(0.6).next_to(eq[2], LEFT)
        rhs[2] = MathTex(r"2",r"\cdot\sin\Big(", r"\frac{1}{2}", r"\cdot x\Big)+", r"0").scale(0.6).next_to(eq[2], RIGHT)
        #Set the RHS Colors
        rhs[2][0].set_color(BLUE)
        rhs[2][2].set_color(GREEN)
        rhs[2][4].set_color(RED)

        #Creates the fourth left hand side, and right hand side
        lhs[3] = MathTex(r"y", ).scale(0.6).next_to(eq[3], LEFT)
        rhs[3] = MathTex(r"2",r"\cdot\sin\Big(", r"\frac{1}{2}", r"\cdot x\Big)-", r"3").scale(0.6).next_to(eq[3], RIGHT)
        #Set the RHS Colors
        rhs[3][0].set_color(BLUE)
        rhs[3][2].set_color(GREEN)
        rhs[3][4].set_color(RED)

        #Creates the fifth left hand side, and right hand side
        lhs[4] = MathTex(r"y", ).scale(0.6).next_to(eq[4], LEFT)
        rhs[4] = MathTex(r"-\frac{1}{3}",r"\cdot\sin(", r"-2", r"\cdot x)+", r"2").scale(0.6).next_to(eq[4], RIGHT)
        #Set the RHS Colors
        rhs[4][0].set_color(BLUE)
        rhs[4][2].set_color(GREEN)
        rhs[4][4].set_color(RED)




        

        
        #################### ANIMATION ###########################

        #Creates the title, and coordinate plane
        self.play( Write(title), Create(axes), Create(numberplane), )# Create(fun))
        #Pause for 3 seconds
        self.wait(3)

        #Write first equation
        self.play(Write(lhs[0]))
        self.wait(2)
        self.play(Write(eq[0]), Write(rhs[0]))
        self.wait(2)
        #Draw the function
        self.play(Create(plot1))
        self.wait(5)


        #setting up a loop for values 1 through 4:
        for i in range(4):
            #Write first equation
            self.play(Write(lhs[i+1]))
            self.wait(2)
            self.play(Write(eq[i+1]), Write(rhs[i+1]))
            self.wait(2)
            #Change the plot over 2 seconds
            self.play(tracka.animate.set_value(a[i+1]), 
                trackb.animate.set_value(b[i+1]),
                trackc.animate.set_value(c[i+1]),
                run_time=2)
            self.wait(5)

        

        self.wait(10)        



class Riemann(Scene):
    def construct(self):

        #Create Title at the top
        title = MathTex(r"R_n, \text{where } n=", color=TEAL).scale(0.8).to_edge(UP)
        #Create #caption at the bottom
        caption = MathTex(r"R_n \approx", color=ORANGE).scale(0.8).to_edge(DOWN)


        #Set up the lowest and greatest x values of our region as well as where the tick marks on the axis go
        xmin = 0
        xmax = 2
        xtick = 0.5

        #Set up the lowest and greatest y values of our region as well as where the tick marks on the axis go
        ymin = 0
        ymax = 20
        ytick = 5


        #Create plane
        axes = Axes(x_range=[xmin,xmax,xtick], y_range=[ymin,ymax,ytick], x_length=6, y_length=5,)
        axes_labels = axes.get_axis_labels(MathTex("x").scale(0.5), MathTex("y").scale(0.5))
        numberplane = NumberPlane(x_range=[xmin,xmax,xtick], y_range=[ymin,ymax,ytick],
            x_length=6,
            y_length=5,
            ).add_coordinates()

        
        
        
        #Create the plot of the function
        plot1 = axes.plot(lambda x: 6*x**3-9*x**2+3, 
            x_range=[0, 2], 
            use_smoothing=True,
            color=YELLOW)
        #label for the plot
        plotlabel = MathTex("f(x)=6x^3-9x^2+3").scale(0.5).next_to(plot1, RIGHT, buff=0.5).set_color(YELLOW)

        #Create 6 riemann rectangles
        rectangles = numberplane.get_riemann_rectangles(plot1, x_range= [0, 2 ], dx=(2-0)/6, color=RED, fill_opacity=0.6, input_sample_type="right")
        #set n = 6
        tracker=ValueTracker(6)

        #update rectangles        
        def updaterectangles(mob):
            mob.become(
                numberplane.get_riemann_rectangles(plot1, 
                    x_range= [0, 2 ], 
                    dx=(2-0)/np.floor(tracker.get_value()), 
                    color=RED, fill_opacity=0.6, input_sample_type="right")
                
        )
        

        rectangles.add_updater(updaterectangles)

        #Creates n in the title next to n= and updates it
        number=DecimalNumber(
            6,
            show_ellipsis=False,
            num_decimal_places=0,
            include_sign=False,
            color=TEAL,
        ).scale(0.8).next_to(title, RIGHT)
        def updateNum(mob):
            mob.become(DecimalNumber(
            np.floor(tracker.get_value()),
            show_ellipsis=False,
            num_decimal_places=0,
            include_sign=False,
            color=TEAL,
        )).scale(0.7).next_to(title, RIGHT)
        number.add_updater(updateNum)


        #Creates R_n in the title next to R_n= and updates it
        number2=DecimalNumber(
            8.3333,
            show_ellipsis=True,
            num_decimal_places=4,
            include_sign=False,
            color=ORANGE
        ).scale(0.8).next_to(caption, RIGHT)
        def updateNum2(mob):
            n = np.floor(tracker.get_value())
            mob.become(DecimalNumber(
            6*((n)**2+2*(n)+2 )/((n)**2),
            show_ellipsis=True,
            num_decimal_places=4,
            include_sign=False,
            color=ORANGE
        )).scale(0.7).next_to(caption, RIGHT)
        number2.add_updater(updateNum2)


        

        self.add(axes, axes_labels, numberplane, title, rectangles, plot1, plotlabel, number, caption, number2)
        self.wait(5)
        #set n = 20
        self.play(tracker.animate.set_value(20), run_time=5)        
        self.wait(3)
        #set n = 500
        self.play(tracker.animate.set_value(500), run_time=5)        
        self.wait(3)
        #set n = 1
        self.play(tracker.animate.set_value(1), run_time=5)
        self.wait(3)
        #set n = 6
        self.play(tracker.animate.set_value(6), run_time=2)
        self.wait(5)                

