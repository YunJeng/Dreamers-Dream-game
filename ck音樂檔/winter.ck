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

[57,62,64,65,67,69]@=> int notelist[];
[0.3,0.2,0.1,0.1,0.1,0.1]@=> float gainArray[];
[0,3,1,2,5,4,3,2] @=> int fadeInOrder[];
0.05 => float overallGain;
0.05 => float gainStep;


for (0 => int j; j < fadeInOrder.cap(); j++) {
    fadeInOrder[j] => int idx;
    Std.mtof(notelist[idx]) => float freq;

    // 判斷是否為長音
    0.5::second => dur noteduration;
    if (idx == 0 || idx == 5) {
        2::second => noteduration;
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

0=> int A;
0=> int E;
0=> int F;
0=> int idx;
[50,53,57]@=> int dmin[];
[53,57,60]@=> int fmaj[];
[52,56,59]@=> int emaj[];
[45,48,52]@=> int amin[];
[55,59,62]@=> int gmaj[];



while(true)
{
    notelist[idx]=> int hz;
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
        s[i].noteOn(0.5);
        
    }
    
    if( hz%12==9){
        if(A==0)
    {
        for (0=> int i; i< c.cap();i++)
   {
    Std.mtof(amin[i])=>c[i].freq;
    0.05=> c[i].gain;
       1=> c[i].noteOn;
    }
   
    2::second => now;
    3 =>  idx;
    1=> A;
}
    else
    {
        for (0=> int i; i< c.cap();i++)
   {
    Std.mtof(amin[i])=>c[i].freq;
    0.05=> c[i].gain;
       1=> c[i].noteOn;
    }
   
    2::second => now;
    4 =>  idx;
    0=> A;
}
}
    else if ( hz%12==5){
        if (F==0)
    {
        for (0=> int i; i< c.cap();i++)
   {
    Std.mtof(fmaj[i])=>c[i].freq;
    0.4=> c[i].gain;
       1=> c[i].noteOn;
    }
    
   0.5::second => now;
    1=>  idx;
    1=> F;
}
    else
    {
        for (0=> int i; i< c.cap();i++)
   {
    Std.mtof(fmaj[i])=>c[i].freq;
    0.4=> c[i].gain;
       1=> c[i].noteOn;
    }
    
   0.5::second => now;
    2=>  idx;
    0=> F;
}
}
    else if (hz%12==2)
    {
        for (0=> int i; i< c.cap();i++)
   {
    Std.mtof(dmin[i])=>c[i].freq;
    0.4=> c[i].gain;
       1=> c[i].noteOn;
       }
      
       0.5::second => now;
       2 =>  idx;
   }
    else if (hz%12==4){
        if (E==0)
    {
        for (0=> int i; i< c.cap();i++)
   {
    Std.mtof(emaj[i])=>c[i].freq;
    0.4=> c[i].gain;
       1=> c[i].noteOn;
    }
    0.5::second => now;
    5=>  idx;
    1=> E;
}
   else
    {
        for (0=> int i; i< c.cap();i++)
   {
    Std.mtof(emaj[i])=>c[i].freq;
    0.4=> c[i].gain;
       1=> c[i].noteOn;
    }
    0.5::second => now;
    0=>  idx;
    0=> E;
}
}
    else if (hz%12==7)
    {
        for (0=> int i; i< c.cap();i++)
   {
    Std.mtof(gmaj[i])=>c[i].freq;
    0.4=> c[i].gain;
       1=> c[i].noteOn;
    }
    0.5::second => now;
    3=>  idx;
}
    else
    {Math.random2(0,5)=> idx;
        }
    
}


