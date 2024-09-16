namespace Futebol_Varzea
{
    partial class Form1
    {
        /// <summary>
        /// Variável de designer necessária.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Limpar os recursos que estão sendo usados.
        /// </summary>
        /// <param name="disposing">true se for necessário descartar os recursos gerenciados; caso contrário, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Código gerado pelo Windows Form Designer

        /// <summary>
        /// Método necessário para suporte ao Designer - não modifique 
        /// o conteúdo deste método com o editor de código.
        /// </summary>
        private void InitializeComponent()
        {
            this.btnCadastrarTime = new System.Windows.Forms.Button();
            this.btnCadastrarPessoas = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // btnCadastrarTime
            // 
            this.btnCadastrarTime.Location = new System.Drawing.Point(438, 310);
            this.btnCadastrarTime.Name = "btnCadastrarTime";
            this.btnCadastrarTime.Size = new System.Drawing.Size(119, 23);
            this.btnCadastrarTime.TabIndex = 0;
            this.btnCadastrarTime.Text = "Cadastrar Time";
            this.btnCadastrarTime.UseVisualStyleBackColor = true;
            this.btnCadastrarTime.Click += new System.EventHandler(this.btnCadastrarTime_Click);
            // 
            // btnCadastrarPessoas
            // 
            this.btnCadastrarPessoas.Location = new System.Drawing.Point(609, 310);
            this.btnCadastrarPessoas.Name = "btnCadastrarPessoas";
            this.btnCadastrarPessoas.Size = new System.Drawing.Size(129, 23);
            this.btnCadastrarPessoas.TabIndex = 1;
            this.btnCadastrarPessoas.Text = "Cadastrar Pessoas";
            this.btnCadastrarPessoas.UseVisualStyleBackColor = true;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(800, 450);
            this.Controls.Add(this.btnCadastrarPessoas);
            this.Controls.Add(this.btnCadastrarTime);
            this.Name = "Form1";
            this.Text = "Form1";
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Button btnCadastrarTime;
        private System.Windows.Forms.Button btnCadastrarPessoas;
    }
}

