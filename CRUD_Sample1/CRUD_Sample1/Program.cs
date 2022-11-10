using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Data.SqlClient;
using System.Data;


namespace CRUD_Sample1
{
    internal class Program
    {
        private const string ConnectionString = "Server=tcp:labuser40sqlserver.database.windows.net,1433;Initial Catalog=labuser40sql;Persist Security Info=False;User ID=oga;Password=Og12345678910;MultipleActiveResultSets=False;Encrypt=True;TrustServerCertificate=False;Connection Timeout=30;";
        private 
            static void Main(string[] args)
        {
            /*System.Data.SqlClient.   이거 안써도됨*/

            SqlConnection con = new SqlConnection(ConnectionString);
            SqlCommand cmd = con.CreateCommand();
            IDataReader reader = null;

            string query = "SELECT * FROM production.brands where brand_id > 5";
            cmd.CommandText = query;
            cmd.Parameters.Add(new SqlParameter("@id", SqlDbType.Int)).Value= 5;

            con.Open();
            Console.WriteLine("Database Connected");
            reader = cmd.ExecuteReader();

            while(reader.Read())
            {
                Console.WriteLine("{0} - {1}", reader.GetInt32(0), reader.GetString(1));
            }
            

            con.Close();
            Console.ReadLine();

        }
    }
}
