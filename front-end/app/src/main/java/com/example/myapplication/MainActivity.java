package com.example.myapplication;

import androidx.appcompat.app.AppCompatActivity;

import android.graphics.drawable.Icon;
import android.os.Bundle;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.SeekBar;
import android.widget.TextView;

import java.lang.reflect.Modifier;
import java.util.Objects;

public class MainActivity extends AppCompatActivity {

    ImageView musicImage;
    TextView musicTitle, musicTimePass, musicTimeRest;
    SeekBar musicSeekBar;
    Button buttonPlay, buttonPrevious, buttonNext, buttonSppeech;

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
        buttonSppeech = findViewById(R.id.button_speech);

        musicTitle.setSelected(true);


    }
}