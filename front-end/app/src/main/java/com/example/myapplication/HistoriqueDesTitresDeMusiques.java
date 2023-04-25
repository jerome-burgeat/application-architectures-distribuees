package com.example.myapplication;

import java.util.ArrayList;
import java.util.List;

public class HistoriqueDesTitresDeMusiques {
    private List<String> titres;
    private int currentID;

    public HistoriqueDesTitresDeMusiques() {
        titres = new ArrayList<>();
        currentID = -1;
    }

    public List<String> getTitres() {
        return titres;
    }

    public void setTitres(List<String> titres) {
        this.titres = titres;
    }

    public int getCurrentID() {
        return currentID;
    }

    public void setCurrentID(int currentID) {
        this.currentID = currentID;
    }

    public void ajouterTitre(String titre) {
        titres.add(titre);
        currentID++;
    }

    public int chercherTitre(String titre) {
        return titres.indexOf(titre);
    }

    public int chercherTitreJoue(String titre) {
        int index = chercherTitre(titre);
        if (index < currentID) {
            this.currentID = index;
            return index;
        }
        return -1;
    }

    public void jouerMusique(String titre) {
        int index = this.chercherTitreJoue(titre);
        if (index == -1) {
            this.ajouterTitre(titre);
            index = this.chercherTitre(titre);
        }
        this.setCurrentID(index);
    }

    public void musiquePrecedent() {
        if(currentID > 0) {
            this.setCurrentID(currentID-1);
        }
    }
}
