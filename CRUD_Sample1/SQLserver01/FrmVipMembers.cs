using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

using System.Data.SqlClient;

namespace SQLserver01
{
    public partial class FrmVipMembers : Form
    {
        SqlConnection Sqlcon = null;
        private const string CONNECTION_STRING = "Server=tcp:labuser40sqlserver.database.windows.net,1433;Initial Catalog=labuser40sql;Persist Security Info=False;User ID=oga;Password=Og12345678910;MultipleActiveResultSets=False;Encrypt=True;TrustServerCertificate=False;Connection Timeout=30;";
        private SqlConnection SqlCon = null;
        private SqlCommand sqlcmd = null;
        private SqlDataAdapter sqlApt = new SqlDataAdapter();
        private DataSet dataMain = new DataSet();


        public FrmVipMembers()
        {
            InitializeComponent();
        }

        private void btnClose_Click(object sender, EventArgs e)
        {
            this.Close();
        }

        private void FrmVipMembers_Load(object sender, EventArgs e)
        {
            SqlCon = new SqlConnection(CONNECTION_STRING);
            


            string query = "select * from dbo.VIPmembers";

            SqlCommand cmd = SqlCon.CreateCommand();
            cmd.CommandText = query;
            

            sqlApt.SelectCommand = cmd;
            sqlApt.Fill(dataMain);

            grdmemberlist.DataSource = dataMain.Tables[0];
        }
    }
}
