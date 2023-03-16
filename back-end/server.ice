module ApplicationArchitecturesDistribuees
{

	sequence<byte> byteList;

    interface Server
    {
        void helloWorld(string helloWorld);
		int getNewIndex();
		bool uploadPart(int id, byteList part);
		bool uploadFile(int id, string filename);
        void addMusic(string dataMusic);
        void deleteMusic(string titleMusic);
        void searchMusic(string titleMusic);
        void updateMusicChangeTitle(string titleCurrent, string newTitle);
    }
}