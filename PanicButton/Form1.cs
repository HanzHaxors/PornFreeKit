using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Runtime.InteropServices;
using System.Drawing.Drawing2D;

namespace PanicButton
{
    public partial class MainForm : Form
    {
        [DllImportAttribute("user32.dll")]
        public static extern int SendMessage(IntPtr hWnd, int Msg, int wParam, int lParam);
        [DllImportAttribute("user32.dll")]
        public static extern int SendMessage(IntPtr Hwnd, int Msg, int wParam, [MarshalAs(UnmanagedType.LPWStr)] string lParam);
        [DllImportAttribute("user32.dll")]
        public static extern bool ReleaseCapture();
        [DllImport("Gdi32.dll", EntryPoint = "CreateRoundRectRgn")]
        public static extern IntPtr CreateRoundRectRgn
            (
            int nLeftRect,
            int nTopRect,
            int nRightRect,
            int nBottomRect,
            int nWidthEllipse,
            int nHeightEllipse
            );
        public const int WM_NCLBUTTONDOWN = 0xA1;
        public const int HT_CAPTION = 0x2;

        // You only need to focus on these costumizeable variables
        // Feel free to edit and submit your Pull Request (PR)!
        readonly List<string> categories = new List<string>
        {
            "Challenge",
            "Random Activity"
        };

        readonly Dictionary<string, List<string>> tasks = new Dictionary<string, List<string>>()
        {
            {
                "Challenge" , new List<string>() {
                    "Do 5 Pushups",
                    "Do cold shower and don't get caught by anyone",
                    "Say something religious",
                    "Do 5 wall pushups",
                    "Do 3 pull ups",
                    "Reboot your computer"
                }
            },
            {
                "Random Activity", new List<string>()
                {
                    "Say something religious",
                    "Upvote random /r/pornfree post",
                    "Say thanks to yourself 25 times"
                }
            }
        };

        public MainForm()
        {
            InitializeComponent();

            GraphicsPath path = new GraphicsPath();
            path.AddEllipse(0, 0, Width, Height);
            this.Region = new Region(path);
        }

        private void PanicButton_MouseMove(object sender, MouseEventArgs e)
        {
            // For moving the window
            if (e.Button == MouseButtons.Left)
            {
                ReleaseCapture();
                SendMessage(Handle, WM_NCLBUTTONDOWN, HT_CAPTION, 0);
            }
        }

        private void PanicButton_Click(object sender, EventArgs e)
        {
            // Fun part!
            // Lets go. Button??

            Random random = new Random();
            int index = random.Next(categories.Count);
            int selectedTaskCount = tasks[categories[index]].Count;
            int taskIndex = random.Next(selectedTaskCount);
            MessageBox.Show(null, tasks[categories[index]][taskIndex], $"Panic Button ask you to do {categories[index]}");
        }
    }
}
