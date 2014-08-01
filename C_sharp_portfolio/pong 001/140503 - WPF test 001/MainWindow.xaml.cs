using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;

namespace _140503___WPF_test_001 {
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    /// setting: App.Current.Properties["NameOfProperty"] = 5;

        public class Brick {
            public int row;
            public int col;
            public byte[] rgbColor = new byte[4];
            public int damage = 0;
        }//create brick struct

        public class Ball {
            //store ball position
            public int x = 0;
            public int y = 0;

            //store ball move increments and directions
            public int ballStepX = 5;
            public int ballStepY = 5;
            public int ballDirX = 1;
            public int ballDirY = 1;

            int ballVelocity;
            int ballSpin;
        
            //create control to represent ball in GUI
            public Ellipse ballControl;
        }//create ball class
    public partial class MainWindow : Window {
//*****************************************************************************DEFINE CLASSES

//*****************************************************************************CREATE OBJECTS
        List<Brick> brickList = new List<Brick>();
        List<Ball> ballList = new List<Ball>();
//************************************************************************************DEFINE GLOBALS
        //main windowsize
        double winBottom = 0;
        double winLeft = 0;
        double winHeight = 800;
        double winWidth;

        //Ball paramters
        double ballWidth = 40;
        double ballHeight = 40;
        int numBalls = 11;

        //Brick parameters
        int numRow = 7;
        int numCol = 20;
        int wallStartX = 0;
        int wallStartY = 80;
        int brickHeight = 20;
        int brickWidth = 40;
        int delayTime = 1;
        double rectRotationAngle;
        double rectRotationIncrement = 1;

        //define timer
        private static System.Windows.Threading.DispatcherTimer ballTimer = new System.Windows.Threading.DispatcherTimer();
//*****************************************************************************MAIN FUNCTION
        public MainWindow() {
            //run functions
            InitializeComponent();
            initGUI();
            createBricks();
            createBalls();
            InitializeAndStartBallTimer();
        }//run all functions
        //******************************************************************************INIT GUI
        #region INIT GUI
        public void initGUI(){
            SetWindowSize();
            SetWindowPosition();
    }
        public void SetWindowPosition() {
            Left = 100;
            Top = 0;
        }//set window position
        public void SetWindowSize() {
            winWidth = numCol * brickWidth;
            this.Height = winHeight;
            this.Width = winWidth;
            grid_ballcage.Width = winWidth;
        }//set window size
        #endregion
        //****************************************************************************INIT CONTROLS
        public void initBricks() {
            //create a List of Bricks, given the number of rows and columns
            for (int row = 0; row <= numRow - 1; row++) {
                for (int col = 0; col <= numCol - 1; col++) {
                    Brick myBrick = new Brick();
                    myBrick.row = wallStartY + row * brickHeight;
                    myBrick.col = wallStartX + col * brickWidth;

                    brickList.Add(myBrick);
                }
            }
            brickList.RemoveAt(2);
        }//create the List of Bricks
        public void createBricks() {
            initBricks();//create the 2d wall of bricks and put them in a single List
            //for each brick in brickList, create the GUI control and assign it properties
            Random myRandom = new Random();
            for (int x = 0; x < brickList.Count; x++) {
                int col = brickList[x].col;
                int row = brickList[x].row;

                Button myButton = new Button();
                myButton.HorizontalAlignment = HorizontalAlignment.Left;
                myButton.VerticalAlignment = VerticalAlignment.Top;
                myButton.Height = brickHeight;
                myButton.Width = brickWidth;

                SolidColorBrush brickSolidColorBrush = new SolidColorBrush();
                byte r = (byte)(myRandom.Next(0, (int)255));
                byte g = (byte)(myRandom.Next(0, (int)255));
                byte b = (byte)(myRandom.Next(0, (int)255));
                brickSolidColorBrush.Color = Color.FromArgb(r, g, b, 255);
                myButton.Background = brickSolidColorBrush;

                brickList[x].rgbColor[0] = r;
                brickList[x].rgbColor[1] = g;
                brickList[x].rgbColor[2] = b;
                brickList[x].rgbColor[3] = (byte)255;
                //brickList[x].rgbColor = {r,r,r,r};

                //int[] test = new int[4];
                //test = {1,2,3,4};

                //List<long> test2 = new List<long>();
                //test2 = (1);

                myButton.Margin =
                    new Thickness(col, row, 0, 0);
                grid_ballcage.Children.Add(myButton);
            }
        }//add all the bricks to the grid
        public void createBalls() {//create a Ball object based on the global class

            Random random = new Random();
            for (int i = 0; i < numBalls; i++) {                
                // create an Ellipse control to assign to the Ball object
                Ellipse myEllipse = new Ellipse();
                myEllipse.Height = 25;
                myEllipse.Width = 25;
                myEllipse.Stroke = Brushes.Violet;
                myEllipse.Fill = Brushes.Black;

                //add the new Ellipse to myBall
                Ball myBall = new Ball();
                myBall.ballControl = myEllipse;
                //give the ball a location
                myBall.ballControl.Margin = new Thickness(100, 100, 5, 5);
                myBall.ballControl.HorizontalAlignment = HorizontalAlignment.Left;
                myBall.ballControl.VerticalAlignment = VerticalAlignment.Top;

                myBall.x = 100 * i;
                myBall.y = 10 * i;
                myBall.ballControl.Width = ballWidth;
                myBall.ballControl.Height = ballHeight;


                //generate a random color for each brick
                SolidColorBrush mySolidColorBrush1 = new SolidColorBrush();
                byte r = (byte)random.Next(0, 255);
                byte g = (byte)random.Next(0, 255);
                byte b = (byte)random.Next(0, 255);

                r = (byte)(i * 30);
                mySolidColorBrush1.Color = Color.FromArgb(r, g, b, 255);
                //mySolidColorBrush1.Color = Color.FromArgb(50, 255, 50, 255);
                myBall.ballControl.Fill = mySolidColorBrush1;
                ballList.Add(myBall);
                grid_ballcage.Children.Add(ballList[i].ballControl);
            }
        }//create a List of Balls
//****************************************************************************GAME FUNCTIONS
        public void moveBall() {
            RotateTransform rectRotateTransform = new RotateTransform(rectRotationAngle);

            foreach (Ball thisBall in ballList) {
                //MessageBox.Show(thisBall.x
                thisBall.ballControl.Margin = new Thickness(thisBall.x, thisBall.y, 5, 5);
                thisBall.x += (int)(thisBall.ballStepX * thisBall.ballDirX);
                thisBall.y += (int)(thisBall.ballStepY * thisBall.ballDirY);

                Boolean hit = true;
                Boolean miss = false;
                hit = (thisBall.y >= winHeight - 120 && thisBall.x >= mattButton.Margin.Left && thisBall.x <= mattButton.Margin.Left + mattButton.Width);
                miss = (thisBall.y >= winHeight && (thisBall.x < mattButton.Margin.Left || thisBall.x > mattButton.Margin.Left + mattButton.Width));

                if (thisBall.x <= winLeft) { thisBall.ballDirX *= -1; }
                if (thisBall.x >= winWidth - 100) { thisBall.ballDirX *= -1; }
                if (hit) { thisBall.ballDirY *= -1; }
                if (miss) {
                    thisBall.y = 100;
                    //choose a random starting x position for new ball
                    ///zzz - how do I combine the 2 lines below?
                    Random random = new Random();
                    int randomNumber = random.Next(0, (int)winWidth);
                    thisBall.x = (int)randomNumber;
                }
                if (thisBall.y <= winBottom) { thisBall.ballDirY *= -1; }

                ballRectangle.Width = ballWidth;
                ballRectangle.Height = ballHeight;
                ballRectangle.Margin = new Thickness(ballList[0].x, ballList[0].y, 5, 5);
                rectRotationAngle += rectRotationIncrement;
                ballRectangle.RenderTransform = rectRotateTransform;
            }
        }//move a single Ball
        public void brickCollision(){
            foreach (Brick myBrick in brickList);
                int a = 0;
        }//detect collision with brick
//*****************************************************************************START TIMER
        public void InitializeAndStartBallTimer() {
            ballTimer.Tick += ballTimer_Tick;
            ballTimer.Interval = new TimeSpan(0, 0, 0, 0, delayTime);
            ballTimer.Start();
        }//init timer
        public void ballTimer_Tick(object sender, EventArgs e) {
            moveBall();
        }//run timer + move ball
//******************************************************************************EVENTS
        private void Grid_PreviewKeyDown(object sender, KeyEventArgs e) {
                if (e.Key == Key.Escape)
                    this.Close();
        }//close window on ESC
        private void grid_ballcage_MouseMove(object sender, MouseEventArgs e) {
            Point mypoint = e.GetPosition(this);
            double posX = mypoint.X;
            double paddleWidth = mattButton.Width;
            double paddleLeft = mattButton.Margin.Left;
            double paddleCenter = posX - (paddleWidth / 2);
            mattButton.Margin = new Thickness(paddleCenter, winHeight - 200, 5, 5);
        }//move paddle on mouse


    }
}

///Code Scraps
////create new buttons in real time
//MessageBox.Show(System.Windows.SystemParameters.PrimaryScreenWidth.ToString() + " " + System.Windows.SystemParameters.PrimaryScreenHeight.ToString());
//public void addNewButton2() {
//    // Set properties.
//    //List <Button> thinList = new List<Button>();
//    List<Button> thinList = new List<Button>();
//    List<List<Button>> gridList = new List<List<Button>>();
//    int tableStartX = 0;
//    int tableStartY = 80;
//    int numRow = 5;
//    int numCol = 10;
//    for (int col = 0; col <= numCol - 1; col++) {
//        int a = 9;
//        for (int row = 0; row <= numRow - 1; row++) {
//            Button myButton = new Button();
//            myButton.HorizontalAlignment = HorizontalAlignment.Left;
//            myButton.VerticalAlignment = VerticalAlignment.Top;
//            myButton.Content = "row = " + row.ToString() + " : " + "col = " + col.ToString();
//            myButton.Height = 30;
//            myButton.Width = 100;
//            myButton.Margin =
//                new Thickness(
//                    tableStartX + col * myButton.Width,
//                    tableStartY + row * myButton.Height,
//                    0,
//                   0);
//            grid_ballcage.Children.Add(myButton);
//            thinList.Add(myButton);
//        }
//        gridList.Add(thinList);

//    }
//}

//// Create Image Element
//Image myImage = new Image();
//myImage.Width = 100;
//// Create source
//BitmapImage myBitmapImage = new BitmapImage();
//// BitmapImage.UriSource must be in a BeginInit/EndInit block
//myBitmapImage.BeginInit();
//myBitmapImage.UriSource = new Uri(@"C:\Users\Matt Hill\Google Drive\_programming\C sharp\_my code\140502 - pong\pong 001\140503 - WPF test 001\alien.png");
//// To save significant application memory, set the DecodePixelWidth or   
//// DecodePixelHeight of the BitmapImage value of the image source to the desired  
//// height or width of the rendered image. If you don't do this, the application will  
//// cache the image as though it were rendered as its normal size rather then just  
//// the size that is displayed. 
//// Note: In order to preserve aspect ratio, set DecodePixelWidth 
//// or DecodePixelHeight but not both.
//myBitmapImage.DecodePixelWidth = 200;
//myBitmapImage.EndInit();
////set image source
//myImage.Source = myBitmapImage;
//pic.Source = myBitmapImage;
