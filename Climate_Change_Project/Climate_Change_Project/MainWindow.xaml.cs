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

namespace Climate_Change_Project
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {

        Line cover;
        public MainWindow()
        {
            InitializeComponent();
          
        }

        private void SliderLatitude_ValueChanged(object sender, RoutedPropertyChangedEventArgs<double> e)
        {

        }

        private void SliderLongitude_ValueChanged(object sender, RoutedPropertyChangedEventArgs<double> e)
        {

        }

        private void SliderDistance_ValueChanged(object sender, RoutedPropertyChangedEventArgs<double> e)
        {
            cover = new Line();

            //cover.X1 = Earth.Margin.Left /* - DistanceSlider.Value;*/;
            //cover.Y1 = Earth.Margin.Top + Earth.ActualHeight / 2 - 50 ;

            //cover.X2 = Earth.Margin.Left /* - DistanceSlider.Value;*/;
            //cover.Y2 = Earth.Margin.Top + Earth.ActualHeight / 2 + 50;

            cover.X1 = 0;
            cover.Y1 = 0;

            cover.X2 = canvas.ActualWidth;
            cover.Y2 = canvas.ActualHeight;

           
            cover.StrokeThickness = 1;
            cover.Stroke = Brushes.Black;

            canvas.Children.Add(cover);

        }

        private void SliderTemperature_ValueChanged(object sender, RoutedPropertyChangedEventArgs<double> e)
        {

        }

        private void Button_Click(object sender, RoutedEventArgs e)
        {
            SliderDistance_ValueChanged(null, null);
        }
    }
}
