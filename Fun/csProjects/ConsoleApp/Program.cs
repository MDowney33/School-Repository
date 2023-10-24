namespace MyNamespace
{

    class Grid{
        public int xlen;
        public int ylen;
        public int xsize;
        public int ysize;
        public bool[] gridX;
        public bool[] gridY;
        public static int GridNum = 0;

        public Grid(){
            Console.WriteLine("Give an x and y value for the size of your grid");            
            xsize = Convert.ToInt32(Console.ReadLine());
            ysize = Convert.ToInt32(Console.ReadLine());            
            xlen = xsize+1;
            ylen = ysize+1;
            
            gridX = new bool[xlen];
            gridY = new bool[ylen];
            GridNum++;
        }

        public void Point()
        {
            Console.WriteLine("Give a value for x in your point for grid size of " + xsize);
            int x = Convert.ToInt32(Console.ReadLine());

            Console.WriteLine("Give a value for y in your point for grid size of " + ysize);
            int y = Convert.ToInt32(Console.ReadLine());

            if (x < 0 || x > xsize || y < 0 || y > ysize || xsize! > 0 || ysize! > 0)
            {
                gridX[x] = true;
                gridY[y] = true;
                Console.WriteLine("Grid value (" + x + ", " + y + ") has been plotted");
            }
        }
        public void PrintGrid()
        {   

            int spacesForY = Convert.ToString(ylen).Length - 1;

            for (int i = -1; i < ylen;){

                bool currentY = false;
                
                if (i!=-1){
                    currentY = gridY[i];

                    for (int l = 0; l < xlen;){
                    
                        bool currentX = gridX[l];
                        if (l==0){
                            Console.Write(i + " ");
                        }

                        if (currentX == true && currentY == true){
                            Console.Write("1");
                            Console.Write(" ");
                        } else {                                                        
                            Console.Write("0");
                            Console.Write(" ");
                        }
                        
                        int numlen = l.ToString().Length;
                        
                        if (l>9){
                            Console.Write(" ", numlen);
                        }

                    l++;
                    }
                } else {
                    
                    Console.Write("  ");
                    
                    for (int l = 0; l < xlen;){
                        Console.Write(l + " ");
                        //Console.Write(" ", spacesForY);
                        l++;
                    }

                }
                Console.WriteLine("");
                i++;         
            }
        }
    }

    class Myclass{
        public static void Main(string[] args){
            Grid grid1 = new Grid();
            
            grid1.Point();

            grid1.PrintGrid();
            
            Console.ReadKey();
            Console.WriteLine("");
        }
    }
}
