package com.example.myapplication;

import androidx.appcompat.app.AppCompatActivity;
import androidx.core.app.ActivityCompat;
import androidx.core.content.ContextCompat;

import com.zeroc.Ice.*;

import android.Manifest;
import android.app.Activity;
import android.content.ContentResolver;
import android.content.ContentUris;
import android.content.Context;
import android.content.Intent;
import android.content.pm.PackageManager;
import android.database.Cursor;
import android.graphics.drawable.Icon;
import android.net.Uri;
import android.os.Bundle;
import android.os.Handler;
import android.os.Looper;
import android.provider.MediaStore;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.SeekBar;
import android.widget.TextView;

import org.json.JSONObject;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.lang.Exception;
import java.lang.reflect.Modifier;
import java.util.Objects;

public class MainActivity extends AppCompatActivity  {

    private static final int READ_EXTERNAL_STORAGE_REQUEST_CODE = 1;
    private static final int WRITE_EXTERNAL_STORAGE_REQUEST_CODE = 123;
    com.zeroc.Ice.Communicator communicator;
    ApplicationArchitecturesDistribuees.ServerPrx app;

//    private static final int READ_STORAGE_PERMISSION_CODE = 1;
    private static final int PERMISSIONS_REQUEST_EXTERNAL_STORAGE = 1;

//    private static final int REQUEST_WRITE_STORAGE = 112;

    ImageView musicImage;
    TextView musicTitle, musicTimePass, musicTimeRest;
    SeekBar musicSeekBar;
    Button buttonPlay, buttonPrevious, buttonNext, buttonSpeech;
    File fileMusic;

    String splitStr(String str){
        String[] segments = str.split("/");
        String rslt = segments[segments.length - 1];
//        System.out.println(mediaId);
        return rslt;
    }

    void handleImage(Intent intent) {
        System.out.println("c'est une image!");
        Uri uri = intent.getData();
        String filePath = uri.getPath();
        System.out.println(filePath);
    }

    void handleAudio(Intent intent) throws IOException {
        System.out.println("c'est un audio!");
        System.out.println(intent);

        if (intent.hasExtra(Intent.EXTRA_STREAM)){
            Uri uri = (Uri) intent.getParcelableExtra(Intent.EXTRA_STREAM);
//            System.out.println("Path file is : " + uri.getPath());
            System.out.println(uri.getPath()); // not real path, its path and(/) id of File
//            String[] segments = uri.getPath().split("/");
//            int mediaId = Integer.parseInt(segments[segments.length - 1]);
            int mediaId = Integer.parseInt(splitStr(uri.getPath()));
            System.out.println(mediaId);
            Uri mediaUri = ContentUris.withAppendedId(MediaStore.Audio.Media.EXTERNAL_CONTENT_URI, mediaId);
            String[] projection = { MediaStore.Audio.Media.DATA };
            Cursor cursor = getContentResolver().query(mediaUri, projection, null, null, null);
            if (cursor != null && cursor.moveToFirst()) {
                int pathColumn = cursor.getColumnIndex(MediaStore.Audio.Media.DATA);
                String filePath = cursor.getString(pathColumn);
                cursor.close();

                System.out.println("The real file path is : " + filePath);
                // 在这里使用 filePath 进行文件操作

                fileMusic = new File(filePath);

                System.out.println(fileMusic.getName());

                InputStream fis = new FileInputStream(fileMusic);
                long fileSize = fileMusic.length(); // 获取文件大小，单位为字节
                System.out.println(fileSize);
                byte[] bytes = new byte[(int)fileMusic.length()]; // 创建字节数组，用于存放文件内容
                long quotient = fileSize / 102400;
                long remainder = fileSize % 102400;
//                System.out.println(app.);
                fis.close();

            }
        }
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        Objects.requireNonNull(getSupportActionBar()).hide();

        try
        {
            communicator = com.zeroc.Ice.Util.initialize();
            /**
             * ipv4 -> le réseau que tu utilise (se trouve en tapand 'ipconfig' sur terminal de pc qui tourne serveur)
             * le réseau utilisé de téléphonne qui tourne application doit être sous le même réseau que celui de serveur
             * spécifique pour emulator : 10.0.2.2
             * normalent pour CERI: 10.120.25.149
             */
            String ipv4 = "192.168.1.145";
            com.zeroc.Ice.ObjectPrx base = communicator.stringToProxy("ApplicationArchitecturesDistribuees:default -h " + ipv4 + " -p 10000");
            app = ApplicationArchitecturesDistribuees.ServerPrx.checkedCast(base);
            System.out.println("hello world! ");
            if(app == null)
            {
                throw new Error("Invalid proxy");
            }
        }catch (Exception e){
            System.out.println(e);
        }

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
////                    JSONObject json = new JSONObject();
////                    json.put("title", "test");
////                    json.put("url", "www.goggle2.com");
////                    app.addMusic(json.toString());
//


                app.helloWorld("Hello World!");

                Context context = view.getContext();
                Activity activity = null;
                if (context instanceof Activity) {
                     activity = (Activity) context;
                    // 在这里可以使用activity对象进行操作
                }

                if (ContextCompat.checkSelfPermission(context, Manifest.permission.READ_EXTERNAL_STORAGE)
                        != PackageManager.PERMISSION_GRANTED) {
                    assert activity != null;
                    ActivityCompat.requestPermissions(activity,
                            new String[]{Manifest.permission.READ_EXTERNAL_STORAGE},
                            READ_EXTERNAL_STORAGE_REQUEST_CODE);
                }
                if (ContextCompat.checkSelfPermission(context, Manifest.permission.WRITE_EXTERNAL_STORAGE)
                        != PackageManager.PERMISSION_GRANTED) {
                    assert activity != null;
                    ActivityCompat.requestPermissions(activity,
                            new String[]{Manifest.permission.WRITE_EXTERNAL_STORAGE},
                            WRITE_EXTERNAL_STORAGE_REQUEST_CODE);
                }

                    Intent intent = getIntent();
                    String action = intent.getAction();
                    String type = intent.getType();

                    if (Intent.ACTION_SEND.equals(action) && type != null) {
                        if (type.startsWith("image/")) {
                            // treat image file
                            handleImage(intent);
                        } else if (type.startsWith("audio/")) {
                            // treat audio file
                            try {
                                handleAudio(intent);
                            } catch (IOException e) {
                                e.printStackTrace();
                            }
                        }
                    }

                if (fileMusic != null) {
                    if (fileMusic.exists()) { // 判断文件是否存在
                        try {
                            InputStream fis = new FileInputStream(fileMusic);
                            System.out.println("ta mere");
                            long fileSize = fileMusic.length(); // 获取文件大小，单位为字节
                            System.out.println("file size : " + fileSize);
                            long quotient = fileSize / 102400;
                            long remainder = fileSize % 102400;
                            int id = app.getNewIndex();
                            System.out.println(id);
                            for (int i=0; i<quotient; i++){
                                byte[] bytes = new byte[102400]; // 创建字节数组，用于存放文件内容
                                int bytesRead = 0;
                                while ((bytesRead = fis.read(bytes)) != -1) {
                                    app.uploadPart(id, bytes);
                                }
                            }
                            byte[] bytes = new byte[(int) remainder];
                            fis.read(bytes);
                            app.uploadPart(id, bytes);
                            System.out.println(fis);
                            fis.close(); // 关闭文件输入流
                            app.uploadFile(id, fileMusic.getName());
                        } catch (IOException e) {
                            // 处理异常
                        }
                    } else {
                        System.out.println("File does not exist.");
                    }
                }

            }
        });


    }

    @Override
    public void onRequestPermissionsResult(int requestCode, String[] permissions, int[] grantResults) {
        super.onRequestPermissionsResult(requestCode, permissions, grantResults);

        switch (requestCode) {
            case READ_EXTERNAL_STORAGE_REQUEST_CODE:
                if (grantResults.length > 0 && grantResults[0] == PackageManager.PERMISSION_GRANTED) {
                    // 已经获取到读取存储权限
                    Intent intent = getIntent();
                    String action = intent.getAction();
                    String type = intent.getType();

                    if (Intent.ACTION_SEND.equals(action) && type != null) {
                        if (type.startsWith("image/")) {
                            // treat image file
                            handleImage(intent);
                        } else if (type.startsWith("audio/")) {
                            // treat audio file
                            try {
                                handleAudio(intent);
                            } catch (IOException e) {
                                e.printStackTrace();
                            }
                        }
                    }
                } else {
                    // 未获取到读取存储权限
                    System.out.println("not access to read !");
                }
                break;
            case WRITE_EXTERNAL_STORAGE_REQUEST_CODE:
                if (grantResults.length > 0 && grantResults[0] == PackageManager.PERMISSION_GRANTED) {
                    // 已经获取到写入存储权限
                    if (fileMusic.exists()) { // 判断文件是否存在
                        FileInputStream fis = null; // 创建文件输入流对象
                        try {
                            fis = new FileInputStream(fileMusic);
                        } catch (FileNotFoundException e) {
                            e.printStackTrace();
                        }
                        System.out.println("ta mere");
                        long fileSize = fileMusic.length(); // 获取文件大小，单位为字节
                        System.out.println("File size : " + fileSize);
                        byte[] bytes = new byte[(int)fileMusic.length()]; // 创建字节数组，用于存放文件内容
                        try {
                            fis.read(bytes); // 将文件内容读取到字节数组中
                        } catch (IOException e) {
                            e.printStackTrace();
                        }
                        try {
                            fis.close(); // 关闭文件输入流
                        } catch (IOException e) {
                            e.printStackTrace();
                        }
                        // 处理读取到的文件内容
                        // ...
                    } else {
                        System.out.println("File does not exist.");
                    }
                } else {
                    // 未获取到写入存储权限
                    System.out.println("not access to write !");
                }
                break;
            default:
                break;
        }
    }

}