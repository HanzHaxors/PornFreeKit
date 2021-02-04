
namespace PanicButton
{
    partial class MainForm
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.PanicButton = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // PanicButton
            // 
            this.PanicButton.BackColor = System.Drawing.Color.Red;
            this.PanicButton.FlatAppearance.BorderSize = 0;
            this.PanicButton.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.PanicButton.Font = new System.Drawing.Font("Segoe UI", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.PanicButton.ForeColor = System.Drawing.Color.White;
            this.PanicButton.Location = new System.Drawing.Point(0, 0);
            this.PanicButton.Margin = new System.Windows.Forms.Padding(0);
            this.PanicButton.Name = "PanicButton";
            this.PanicButton.Size = new System.Drawing.Size(64, 64);
            this.PanicButton.TabIndex = 0;
            this.PanicButton.Text = "PANIC";
            this.PanicButton.UseVisualStyleBackColor = false;
            this.PanicButton.Click += new System.EventHandler(this.PanicButton_Click);
            this.PanicButton.MouseMove += new System.Windows.Forms.MouseEventHandler(this.PanicButton_MouseMove);
            // 
            // MainForm
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackColor = System.Drawing.Color.Chocolate;
            this.ClientSize = new System.Drawing.Size(64, 64);
            this.Controls.Add(this.PanicButton);
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.None;
            this.Name = "MainForm";
            this.ShowInTaskbar = false;
            this.StartPosition = System.Windows.Forms.FormStartPosition.Manual;
            this.Text = "Form1";
            this.TopMost = true;
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Button PanicButton;
    }
}

