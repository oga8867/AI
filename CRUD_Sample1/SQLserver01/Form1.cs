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
    public partial class FrmMain : Form
    {
        private const string CONNECTION_STRING = "Server=tcp:labuser40sqlserver.database.windows.net,1433;Initial Catalog=labuser40sql;Persist Security Info=False;User ID=oga;Password=Og12345678910;MultipleActiveResultSets=False;Encrypt=True;TrustServerCertificate=False;Connection Timeout=30;";
        private SqlConnection SqlCon = null;
        private SqlCommand sqlcmd = null;
        private SqlDataAdapter sqlApt = new SqlDataAdapter();
        private DataSet dataMain = new DataSet();

        public FrmMain()
        {
            InitializeComponent();
        }

        private void FrmMain_Load(object sender, EventArgs e)
        {

        }

        private void FrmMain_Click(object sender, EventArgs e)
        {

        }

        private void btmConnect_Click(object sender, EventArgs e)
        {
            SqlCon = new SqlConnection(CONNECTION_STRING);
            btmConnect.Enabled = false;
        }

        private void btmGetData_Click(object sender, EventArgs e)
        {
            string query = "SELECT * FROM production.brands";

            SqlCommand cmd = SqlCon.CreateCommand();
            cmd.CommandText = query;
            cmd.Parameters.Add(new SqlParameter("@id", SqlDbType.Int)).Value = 5;

            sqlApt.SelectCommand = cmd;
            sqlApt.Fill(dataMain);

            lstbrands.Items.Clear();

            DataRowCollection dataRows = dataMain.Tables[0].Rows;

            for(int i = 0; i < dataRows.Count; i++)
            {
                lstbrands.Items.Add(dataRows[i][1].ToString());
            }

            
            //lstbrands.Items.Add("test");
            //fill to DatagridView
            /*DataSet dataProducts = new DataSet();
            query = "SELECT * FROM production.products";
            cmd.CommandText = query;
            sqlApt.Fill(dataProducts);
            grdproducts.DataSource= dataProducts.Tables[0];
            */

            btnGetData.Enabled = false;
        }

        private void lstbrands_SelectedIndexChanged(object sender, EventArgs e)
        {
            //지금 선택되어 있는 값(리스트박스)
            if (lstbrands.SelectedIndex == -1)
            {   
                
                return;
            }
            
            int selectedIndex = lstbrands.SelectedIndex;
            int selectedBrandID = Int32.Parse(dataMain.Tables[0].Rows[selectedIndex][0].ToString()); //int32로 컨버팅 근데 parse는 스트링만 인식함;; 뭐 이런...

            DataSet dataProducts = new DataSet();
            string query = "SELECT * FROM production.products WHERE brand_id = @brand_id";
            SqlCommand cmd = SqlCon.CreateCommand();
            cmd.Parameters.Add(new SqlParameter("@brand_id", SqlDbType.Int)).Value = selectedBrandID;
            cmd.CommandText = query;
            sqlApt.SelectCommand = cmd;
            sqlApt.Fill(dataProducts);
            grdproducts.DataSource = dataProducts.Tables[0];


        }

        private void btnVIPmembers_Click(object sender, EventArgs e)
        {
            FrmVipMembers vip = new FrmVipMembers();
            vip.ShowDialog();
        }
    }
}