Flute s[6]=>dac;
for (0 => int i; i < s.cap(); i++) 
    {
    s[i] => dac;
}

Mandolin c[3]=>dac;
for (0 => int i; i < c.cap(); i++) 
    {
    c[i] => dac;
}

[72,74,77,79,81,84]@=> int notelist[];
[0.3,0.2,0.1,0.1,0.1,0.1]@=> float gainArray[];
[0,3,4,2,1,3,5,4] @=> int fadeInOrder[];
0.2 => float overallGain;
0.05 => float gainStep;


for (0 => int j; j < fadeInOrder.cap(); j++) {
    fadeInOrder[j] => int idx;
    Std.mtof(notelist[idx]) => float freq;

    // 判斷是否為長音
    0.6*0.33::second => dur noteduration;
    if (j%2==0) {
        0.6*0.66::second => noteduration;
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
0=> int C;
0=> int A;
0=> int G;
0=> int idx;
[60,64,67]@=> int cmaj[];
[65,69,72]@=> int fmaj[];
[67,71,74]@=> int gmaj[];
[69,72,76]@=> int amin[];
[62,65,69]@=> int dmin[];


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
        1 => s[i].noteOn;
    }
//chord
    if( hz%12==0)
    {
        if (C==0){
        for (0=> int i; i< c.cap();i++)
   {
    Std.mtof(cmaj[i])=>c[i].freq;
    0.3*0.25=> c[i].gain;
       1 => c[i].pluck;
    }
   
    0.6*0.66::second => now;
    3 =>  idx;
    1=>C;
}
    else{
        for (0=> int i; i< c.cap();i++)
   {
    Std.mtof(cmaj[i])=>c[i].freq;
    0.3*0.25=> c[i].gain;
       1 => c[i].pluck;
    }
   
    0.6*0.66::second => now;
    4 =>  idx;
    0=>C;
}
}
    else if ( hz%12==5)
    {
        for (0=> int i; i< c.cap();i++)
   {
    Std.mtof(fmaj[i])=>c[i].freq;
    0.3*0.5=> c[i].gain;
       1 => c[i].pluck;
    }
    
   0.6*0.33::second => now;
    1=>  idx;
}
    else if ( hz%12==2)
    {
        for (0=> int i; i< c.cap();i++)
   {
    Std.mtof(dmin[i])=>c[i].freq;
    0.3*0.5=> c[i].gain;
       1 => c[i].pluck;
    }
    
   0.6*0.66::second => now;
    3=>  idx;
}
    else if (hz%12==9){
        if (A==0){
        for (0=> int i; i< c.cap();i++)
   {
    Std.mtof(amin[i])=>c[i].freq;
    0.3*0.5=> c[i].gain;
       1 => c[i].pluck;
       }
      
       0.6*0.66::second => now;
       2 =>  idx;
       1=>A;
   }
    else{
        for (0=> int i; i< c.cap();i++)
   {
    Std.mtof(amin[i])=>c[i].freq;
    0.3*0.5=> c[i].gain;
       1 => c[i].pluck;
       }
      
       0.6*0.33::second => now;
       0 =>  idx;
       0=>A;
   }
   }
    else if (hz%12==7){
        if (G==0)
    {
        for (0=> int i; i< c.cap();i++)
   {
    Std.mtof(gmaj[i])=>c[i].freq;
    0.3*0.25=> c[i].gain;
       1 => c[i].pluck;
    }
    0.6*0.33::second => now;
    4=>  idx;
    1=> G;
}
    else
    {
        for (0=> int i; i< c.cap();i++)
   {
    Std.mtof(gmaj[i])=>c[i].freq;
    0.3*0.25=> c[i].gain;
       1 => c[i].pluck;
    }
    0.6*0.33::second => now;
    5=>  idx;
    0=> G;
}
}
    else
    {Math.random2(0,5)=> idx;
        }
    
}


