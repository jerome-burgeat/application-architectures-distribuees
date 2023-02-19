package com.example.myapplication;

import androidx.appcompat.app.AppCompatActivity;

import android.graphics.drawable.Icon;
import android.os.Bundle;
import android.widget.TextView;

import java.lang.reflect.Modifier;

public class MainActivity extends AppCompatActivity {

    TextView musicTitle;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        getSupportActionBar().hide();
        musicTitle = findViewById(R.id.music_title);
        musicTitle.setSelected(true);


    }
}