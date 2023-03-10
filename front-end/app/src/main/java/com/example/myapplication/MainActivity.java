package com.example.myapplication;

import androidx.appcompat.app.AppCompatActivity;

import com.zeroc.Ice.*;
//import Server.*;

import android.graphics.drawable.Icon;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.SeekBar;
import android.widget.TextView;

import java.lang.Exception;
import java.lang.reflect.Modifier;
import java.util.Objects;

public class MainActivity extends AppCompatActivity  {

    ImageView musicImage;
    TextView musicTitle, musicTimePass, musicTimeRest;
    SeekBar musicSeekBar;
    Button buttonPlay, buttonPrevious, buttonNext, buttonSpeech;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        Objects.requireNonNull(getSupportActionBar()).hide();

        musicImage = findViewById(R.id.music_image);
        musicTitle = findViewById(R.id.music_title);
        musicTimePass = findViewById(R.id.music_time_pass);
        musicTimeRest = findViewById(R.id.music_time_rest);
        musicSeekBar = findViewById(R.id.music_seekBar);
        buttonPlay = findViewById(R.id.button_play);
        buttonPrevious = findViewById(R.id.button_previous);
        buttonNext = findViewById(R.id.button_next);
        buttonSpeech = findViewById(R.id.button_speech);

        musicTitle.setSelected(true);

        buttonSpeech.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                System.out.println("hello world! ");
                try
                {
                    com.zeroc.Ice.Communicator communicator = com.zeroc.Ice.Util.initialize();
                    com.zeroc.Ice.ObjectPrx base = communicator.stringToProxy("ApplicationArchitecturesDistribuees:default -h 192.168.1.145 -p 10000");
                    ApplicationArchitecturesDistribuees.ServerPrx app = ApplicationArchitecturesDistribuees.ServerPrx.checkedCast(base);
                    if(app == null)
                    {
                        throw new Error("Invalid proxy");
                    }
                    app.helloWorld("Hello World!");
                }catch (Exception e){
                    System.out.println(e);
                }
            }
        });


    }
}