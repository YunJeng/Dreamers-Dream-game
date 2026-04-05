SinOsc s[6]=>dac;
for (0 => int i; i < s.cap(); i++) 
    {
    s[i] => dac;
}

Mandolin c[4]=>dac;
for (0 => int i; i < c.cap(); i++) 
    {
    c[i] => dac;
}

[67,69,71,72,74,76,78,79]@=> int notelist[];
[0.3,0.2,0.1,0.1,0.1,0.1]@=> float gainArray[];

0=> int C;
0=> int D;
0=> int E;
0=> int G;
0=> int idx;
[60,64,67,72]@=> int cmaj[];
[62,66,69,72]@=> int dmaj[];
[67,71,74,79]@=> int gmaj[];
[64,67,71,76]@=> int emin[];
[69,72,76,81]@=> int amin[];
[71,74,78,83]@=> int bmin[];


while(true)
{
    notelist[idx]=> int hz;
    <<<idx>>>;
    <<<Std.mtof (hz)>>>;
    Std.mtof (hz)=>float _base;
     _base*2 => float _first;
     _base*3=> float _second;
     _base*4 => float _third;
     _base*5=> float _fourth;
     _base*6 => float _fifth;
     
    [ _base, _first,_second,_third,_fourth,_fifth ]@=> float freqArray[];

    for(0 => int i; i<s.cap(); i++)
    {
        freqArray[i] => s[i].freq;
        gainArray[i] *0.4=> s[i].gain;
        //1 => s[i].noteOn;
    }
//chord
    if( hz%12==7)
    {
        if (G==0){
        for (0=> int i; i< c.cap();i++)
   {
    Std.mtof(gmaj[i])=>c[i].freq;
    0.2=> c[i].gain;
       1 => c[i].pluck;
     
    }
   
    0.25::second => now;
    2 =>  idx;
    1=>G;
}
        else if(G==1)
            {
            for (0=> int i; i< c.cap();i++)
       {
        Std.mtof(gmaj[i])=>c[i].freq;
        0.2=> c[i].gain;
           1 => c[i].pluck;
         
        }
       
        0.25::second => now;
        1 =>  idx;
        2=>G;
    }
            
        else{
            for (0=> int i; i< c.cap();i++)
       {
        Std.mtof(gmaj[i])=>c[i].freq;
        0.2=> c[i].gain;
           1 => c[i].pluck;
        }
       
        0.25::second => now;
        0=>  idx;
        0=>G;
    }
}
    else if ( hz%12==9)
    {
        for (0=> int i; i< c.cap();i++)
   {
    Std.mtof(amin[i])=>c[i].freq;
    0.2=> c[i].gain;
       1 => c[i].pluck;
    }
    
   0.25::second => now;
    4=>  idx;
}
    else if ( hz%12==11)
    {
        for (0=> int i; i< c.cap();i++)
   {
    Std.mtof(bmin[i])=>c[i].freq;
    0.2=> c[i].gain;
       1 => c[i].pluck;
    }
    
   0.25::second => now;
    5=>  idx;
}
    else if ( hz%12==2){
        if (D==0)
    {
        for (0=> int i; i< c.cap();i++)
   {
    Std.mtof(dmaj[i])=>c[i].freq;
    0.2=> c[i].gain;
       1 => c[i].pluck;
    }
    
  0.25::second => now;
    3=>  idx;
    1=>D;
}
        else if (D==1)
    {
        for (0=> int i; i< c.cap();i++)
   {
    Std.mtof(dmaj[i])=>c[i].freq;
    0.2=> c[i].gain;
       1 => c[i].pluck;
    }
    
   0.25::second => now;
    5=>  idx;
    2=>D;
}
        else 
    {
        for (0=> int i; i< c.cap();i++)
   {
    Std.mtof(dmaj[i])=>c[i].freq;
    0.2=> c[i].gain;
       1 => c[i].pluck;
    }
    
   0.25::second => now;
    7=>  idx;
    0=>D;
}
}
    else if (hz%12==4){
        if (E==0){
        for (0=> int i; i< c.cap();i++)
   {
    Std.mtof(emin[i])=>c[i].freq;
    0.2=> c[i].gain;
      1 => c[i].pluck;
       }
      
       0.25::second => now;
       4 =>  idx;
       1=>E;
   }
    else{
        for (0=> int i; i< c.cap();i++)
   {
    Std.mtof(emin[i])=>c[i].freq;
    0.2=> c[i].gain;
       1 => c[i].pluck;
       }
      
       0.25::second => now;
       3 =>  idx;
       0=>E;
   }
   }
    else if (hz%12==0){
        if (C==0)
    {
        for (0=> int i; i< c.cap();i++)
   {
    Std.mtof(cmaj[i])=>c[i].freq;
    0.2=> c[i].gain;
       1 => c[i].pluck;
    }
    0.25::second => now;
    0=>  idx;
    1=> C;
}
    else
    {
        for (0=> int i; i< c.cap();i++)
   {
    Std.mtof(cmaj[i])=>c[i].freq;
    0.2=> c[i].gain;
       1 => c[i].pluck;
    }
    0.25::second => now;
    4=>  idx;
    0=> C;
}
}
    else
    {Math.random2(0,5)=> idx;
        }
    
}


