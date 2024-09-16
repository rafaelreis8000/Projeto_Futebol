using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Futebol_Varzea
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void btnCadastrarTime(object sender, EventArgs e)
        {
            string nomeTime = Microsoft.VisualBasic.Interaction.InputBox("Digite o nome do Time:", "Cadastro de Time", "", -1, -1);

            if (!string.IsNullOrEmpty(nomeTime))
            {
                MessageBox.Show($"Time {nomeTime} cadastrado com sucesso!");
            }
            else
            {
                MessageBox.Show("Cadastro de Time cancelado ou inválido.");
            }
        }
        private void button2_Click(object sender, EventArgs e)
        {
            string nomePessoa = Microsoft.VisualBasic.Interaction.InputBox("Digite o nome da Pessoa:", "Cadastro de Pessoa", "", -1, -1);

            if (!string.IsNullOrEmpty(nomePessoa))
            {
                MessageBox.Show($"Pessoa {nomePessoa} cadastrada com sucesso!");
            }
            else
            {
                MessageBox.Show("Cadastro de Pessoa cancelado ou inválido.");
            }
        }

    }
}