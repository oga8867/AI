namespace SQLserver01
{
    partial class FrmMain
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
            this.btmConnect = new System.Windows.Forms.Button();
            this.btnGetData = new System.Windows.Forms.Button();
            this.lstbrands = new System.Windows.Forms.ListBox();
            this.grdproducts = new System.Windows.Forms.DataGridView();
            this.btnVIPmembers = new System.Windows.Forms.Button();
            ((System.ComponentModel.ISupportInitialize)(this.grdproducts)).BeginInit();
            this.SuspendLayout();
            // 
            // btmConnect
            // 
            this.btmConnect.Location = new System.Drawing.Point(12, 12);
            this.btmConnect.Name = "btmConnect";
            this.btmConnect.Size = new System.Drawing.Size(75, 23);
            this.btmConnect.TabIndex = 0;
            this.btmConnect.Text = "connect";
            this.btmConnect.UseVisualStyleBackColor = true;
            this.btmConnect.Click += new System.EventHandler(this.btmConnect_Click);
            // 
            // btnGetData
            // 
            this.btnGetData.Location = new System.Drawing.Point(12, 41);
            this.btnGetData.Name = "btnGetData";
            this.btnGetData.Size = new System.Drawing.Size(75, 23);
            this.btnGetData.TabIndex = 1;
            this.btnGetData.Text = "Get Data";
            this.btnGetData.UseVisualStyleBackColor = true;
            this.btnGetData.Click += new System.EventHandler(this.btmGetData_Click);
            // 
            // lstbrands
            // 
            this.lstbrands.FormattingEnabled = true;
            this.lstbrands.Location = new System.Drawing.Point(33, 114);
            this.lstbrands.Name = "lstbrands";
            this.lstbrands.Size = new System.Drawing.Size(132, 290);
            this.lstbrands.TabIndex = 2;
            this.lstbrands.SelectedIndexChanged += new System.EventHandler(this.lstbrands_SelectedIndexChanged);
            // 
            // grdproducts
            // 
            this.grdproducts.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.grdproducts.Location = new System.Drawing.Point(190, 12);
            this.grdproducts.Name = "grdproducts";
            this.grdproducts.Size = new System.Drawing.Size(588, 415);
            this.grdproducts.TabIndex = 3;
            // 
            // btnVIPmembers
            // 
            this.btnVIPmembers.Location = new System.Drawing.Point(12, 70);
            this.btnVIPmembers.Name = "btnVIPmembers";
            this.btnVIPmembers.Size = new System.Drawing.Size(100, 23);
            this.btnVIPmembers.TabIndex = 4;
            this.btnVIPmembers.Text = "VIP management";
            this.btnVIPmembers.UseVisualStyleBackColor = true;
            this.btnVIPmembers.Click += new System.EventHandler(this.btnVIPmembers_Click);
            // 
            // FrmMain
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(800, 450);
            this.Controls.Add(this.btnVIPmembers);
            this.Controls.Add(this.grdproducts);
            this.Controls.Add(this.lstbrands);
            this.Controls.Add(this.btnGetData);
            this.Controls.Add(this.btmConnect);
            this.Name = "FrmMain";
            this.Text = "welcome to SQL Server Tester";
            this.Load += new System.EventHandler(this.FrmMain_Load);
            this.Click += new System.EventHandler(this.FrmMain_Click);
            ((System.ComponentModel.ISupportInitialize)(this.grdproducts)).EndInit();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Button btmConnect;
        private System.Windows.Forms.Button btnGetData;
        private System.Windows.Forms.ListBox lstbrands;
        private System.Windows.Forms.DataGridView grdproducts;
        private System.Windows.Forms.Button btnVIPmembers;
    }
}

