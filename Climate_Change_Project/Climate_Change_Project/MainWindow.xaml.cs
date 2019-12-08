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

            Thickness m = Screen.Margin;

            m.Top = 2 * e.NewValue + 144;

            Screen.Margin = m;
            
        }

        private void SliderDistance_ValueChanged(object sender, RoutedPropertyChangedEventArgs<double> e)
        {
            Thickness m = Screen.Margin;
            
            m.Left = 15 * e.NewValue + 250;

            Screen.Margin = m;
        }

        private void SliderTemperature_ValueChanged(object sender, RoutedPropertyChangedEventArgs<double> e)
        {
           

        }       
    }
}
