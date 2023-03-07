module ApplicationArchitecturesDistribuees
{
    interface Server
    {
        void helloWorld(string helloWorld);
        void addMusic(string dataMusic);
        void deleteMusic(string titleMusic);
        void searchMusic(string titleMusic);
        void updateMusicChangeTitle(string titleCurrent, string newTitle);
    }
}