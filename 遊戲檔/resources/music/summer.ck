Saxofony s[6]=>dac;
for (0 => int i; i < s.cap(); i++) 
    {
    s[i] => dac;
}

Wurley c[3]=>dac;
for (0 => int i; i < c.cap(); i++) 
    {
    c[i] => dac;
    
}

[69,71,74,76,78,81]@=> int notelist[];
[0.3,0.2,0.1,0.1,0.1,0.1]@=> float gainArray[];
[0,3,4,2,1,3,5,2] @=> int fadeInOrder[];
0.025 => float overallGain;
0.05 => float gainStep;


for (0 => int j; j < fadeInOrder.cap(); j++) {
    fadeInOrder[j] => int idx;
    Std.mtof(notelist[idx]) => float freq;

    // 判斷是否為長音
    0.25::second => dur noteduration;
    

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

0=> int A;
0=> int E;
0=> int D;
0=> int idx;
[57,61,64]@=> int amaj[];
[62,66,69]@=> int dmaj[];
[64,68,71]@=> int emaj[];
[66,69,73]@=> int fmin[];
[59,62,66]@=> int bmin[];


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
        gainArray[i] => s[i].gain;
        s[i].noteOn(0.3);
        
    }
//chord
    if( hz%12==9){
        if (A==0){
        for (0=> int i; i< c.cap();i++)
   {
    Std.mtof(amaj[i])=>c[i].freq;
    0.05=> c[i].gain;
       1=> c[i].noteOn;
    }
   
    250::ms => now;
    3 =>  idx;
    1=> A;
}
        else{
        for (0=> int i; i< c.cap();i++)
   {
    Std.mtof(amaj[i])=>c[i].freq;
    0.15=> c[i].gain;
       1=> c[i].noteOn;
    }
   
    250::ms => now;
    2 =>  idx;
    0=> A;
}
}
    else if ( hz%12==4){
        if (E==0)
    {
        for (0=> int i; i< c.cap();i++)
   {
    Std.mtof(emaj[i])=>c[i].freq;
    0.15=> c[i].gain;
       1=> c[i].noteOn;
    }
    
   250::ms => now;
    4=>  idx;
    1=>E;
}
        else
       {
        for (0=> int i; i< c.cap();i++)
   {
    Std.mtof(emaj[i])=>c[i].freq;
    0.2=> c[i].gain;
       1=> c[i].noteOn;
    }
    
   250::ms => now;
    5=>  idx;
    0=>E;
}
}
    else if (hz%12==6)
    {
        for (0=> int i; i< c.cap();i++)
   {
    Std.mtof(fmin[i])=>c[i].freq;
    0.15=> c[i].gain;
       1=> c[i].noteOn;
       }
      
       250::ms => now;
       2 =>  idx;
   }
   else if (hz%12==11)
    {
        for (0=> int i; i< c.cap();i++)
   {
    Std.mtof(bmin[i])=>c[i].freq;
    0.25=> c[i].gain;
       1=> c[i].noteOn;
       }
      
       250::ms => now;
       3 =>  idx;
   }
    else if (hz%12==2){
        if (D==0)
    {
        for (0=> int i; i< c.cap();i++)
   {
    Std.mtof(dmaj[i])=>c[i].freq;
    0.2=> c[i].gain;
       1=> c[i].noteOn;
    }
    250::ms => now;
    1=>  idx;
    1=>D;
}
        else
    {
        for (0=> int i; i< c.cap();i++)
   {
    Std.mtof(dmaj[i])=>c[i].freq;
    0.1=> c[i].gain;
       1=> c[i].noteOn;
    }
    250::ms => now;
    0=>  idx;
    0=>D;
}
}
    else
    {Math.random2(0,4)=> idx;
        }
    
}


