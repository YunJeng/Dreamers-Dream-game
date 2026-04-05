Clarinet s[6]=>dac;
for (0 => int i; i < s.cap(); i++) 
    {
    s[i] => dac;
}

Wurley c[3]=>dac;
for (0 => int i; i < c.cap(); i++) 
    {
    c[i] => dac;
    
}

[62,65,67,69,70,73,74]@=> int notelist[];
[0.3,0.2,0.1,0.1,0.1,0.1]@=> float gainArray[];
[0,4,1,5,2,3,0,6] @=> int fadeInOrder[];
0.03 => float overallGain;
0.015 => float gainStep;


for (0 => int j; j < fadeInOrder.cap(); j++) {
    fadeInOrder[j] => int idx;
    Std.mtof(notelist[idx]) => float freq;

    // 判斷是否為長音
    0.5::second => dur noteduration;
    if (j==0||j==2) {
        1::second => noteduration;
    }

   // 設定音高與目前總 gain
    for (0 => int i; i < s.cap(); i++) {
        freq => s[i].freq;
        (gainArray[i] * overallGain) => s[i].gain;
        s[i].noteOn(0.5);
    }

    // 播完這個音
    noteduration => now;

    // 累加整體 gain（漸強）
    overallGain + gainStep => overallGain;
    if (overallGain > 1.0) {
        1.0 => overallGain;
    }
       

    // 結束這個 note
    for (0 => int i; i < s.cap(); i++) {
        s[i].noteOff(0.3);
    }

    1::ms => now;
}
0=> int D;
0=> int idx;
[62,65,69]@=> int dmin[];
[58,62,65]@=> int bmaj[];
[53,57,60]@=> int fmaj[];
[61,64,67]@=> int cmin[];
[55,58,62]@=> int gmin[];
[57,61,64]@=> int amaj[];

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
        gainArray[i]*0.5 => s[i].gain;
        s[i].noteOn(0.4);
        
    }
//chord
    if( hz%12==2){
        if(D==0)
    {
        for (0=> int i; i< c.cap();i++)
   {
    Std.mtof(dmin[i])=>c[i].freq;
    0.05=> c[i].gain;
       1=> c[i].noteOn;
    }
   
    1::second => now;
    4 =>  idx;
    1=>D;
}
       else if (D==1)
    {
        for (0=> int i; i< c.cap();i++)
   {
    Std.mtof(dmin[i])=>c[i].freq;
    0.04=> c[i].gain;
       1=> c[i].noteOn;
    }
   
    0.5::second => now;
    6 =>  idx;
    2=>D;
}
     else 
    {
        for (0=> int i; i< c.cap();i++)
   {
    Std.mtof(dmin[i])=>c[i].freq;
    0.05=> c[i].gain;
       1=> c[i].noteOn;
    }
   
    1::second => now;
    0 =>  idx;
    0=>D;
}
}

    else if ( hz%12==10)
    {
        for (0=> int i; i< c.cap();i++)
   {
    Std.mtof(bmaj[i])=>c[i].freq;
    0.015=> c[i].gain;
       1=> c[i].noteOn;
    }
    
   0.5::second => now;
    1=>  idx;
}
    else if (hz%12==5)
    {
        for (0=> int i; i< c.cap();i++)
   {
    Std.mtof(fmaj[i])=>c[i].freq;
    0.025=> c[i].gain;
       1=> c[i].noteOn;
       }
      
       1::second => now;
       5 =>  idx;
   }
    else if (hz%12==1)
    {
        for (0=> int i; i< c.cap();i++)
   {
    Std.mtof(cmin[i])=>c[i].freq;
    0.005=> c[i].gain;
       1=> c[i].noteOn;
    }
    0.5::second => now;
    2=>  idx;
}
    else if (hz%12==7)
    {
        for (0=> int i; i< c.cap();i++)
   {
    Std.mtof(gmin[i])=>c[i].freq;
    0.01=> c[i].gain;
       1=> c[i].noteOn;
    }
    0.5::second => now;
    3=>  idx;
}
    else if (hz%12==9)
    {
        for (0=> int i; i< c.cap();i++)
   {
    Std.mtof(amaj[i])=>c[i].freq;
    0.025=> c[i].gain;
       1=> c[i].noteOn;
    }
    0.5::second => now;
    0=>  idx;
}
    else
    {Math.random2(0,4)=> idx;
        }
    
}


