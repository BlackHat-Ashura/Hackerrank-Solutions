#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>
#define MAX_CHARACTERS 1005
#define MAX_PARAGRAPHS 5

struct word {
    char* data;
};

struct sentence {
    struct word* data;
    int word_count;//denotes number of words in a sentence
};

struct paragraph {
    struct sentence* data  ;
    int sentence_count;//denotes number of sentences in a paragraph
};

struct document {
    struct paragraph* data;
    int paragraph_count;//denotes number of paragraphs in a document
};

struct document get_document(char* text) {
    int current_paragraph = 0, current_sentence = 0, current_word = 0, current_letter = 0;
    
    struct document Doc;
    Doc.data = (struct paragraph *)malloc(sizeof(struct paragraph));
    Doc.data[0].data = (struct sentence *)malloc(sizeof(struct sentence));
    Doc.data[0].data[0].data = (struct word *)malloc(sizeof(struct word));
    Doc.data[0].data[0].data[0].data = (char *)malloc(sizeof(char));
    
    for(int i = 0; i < strlen(text); i++) {
        if(text[i] == '\n') {
            if(i == strlen(text) - 1) break;
            current_paragraph++;
            
            current_sentence = current_word = current_letter = 0;
            
            Doc.data = (struct paragraph *)realloc(Doc.data, sizeof(struct paragraph) * (current_paragraph + 1));
            Doc.paragraph_count = current_paragraph;
            
            Doc.data[current_paragraph].data = (struct sentence *)malloc(sizeof(struct sentence));
            Doc.data[current_paragraph].sentence_count = 0;
            
            Doc.data[current_paragraph].data[0].data = (struct word *)malloc(sizeof(struct word));
            Doc.data[current_paragraph].data[0].word_count = 0;
            
            Doc.data[current_paragraph].data[0].data[0].data = (char *)malloc(sizeof(char));
        }
        else if(text[i] == '.') {
            Doc.data[current_paragraph].data[current_sentence].word_count++;
            current_sentence++;
            
            current_word = current_letter = 0;
            
            Doc.data[current_paragraph].data = (struct sentence *)realloc(Doc.data[current_paragraph].data, sizeof(struct sentence) * (current_sentence + 1));
            Doc.data[current_paragraph].sentence_count = current_sentence;
            
            Doc.data[current_paragraph].data[current_sentence].data = (struct word *)malloc(sizeof(struct word));
            Doc.data[current_paragraph].data[current_sentence].word_count = 0;
            
            Doc.data[current_paragraph].data[current_sentence].data[0].data = (char *)malloc(sizeof(char));
        }
        else if(text[i] == ' ') {
            current_word++;
            
            current_letter = 0;
            
            Doc.data[current_paragraph].data[current_sentence].data = (struct word *)realloc(Doc.data[current_paragraph].data[current_sentence].data, sizeof(struct word) * (current_word + 1));
            Doc.data[current_paragraph].data[current_sentence].word_count = current_word;
            
            Doc.data[current_paragraph].data[current_sentence].data[current_word].data = (char *)malloc(sizeof(char));
        }
        else {
            Doc.data[current_paragraph].data[current_sentence].data[current_word].data[current_letter] = text[i];
            current_letter++;
            
            Doc.data[current_paragraph].data[current_sentence].data[current_word].data = (char *)realloc(Doc.data[current_paragraph].data[current_sentence].data[current_word].data, sizeof(char) * (current_letter + 1));
            
            Doc.data[current_paragraph].data[current_sentence].data[current_word].data[current_letter] = '\0';
        }
    }
    return Doc;
}

struct word kth_word_in_mth_sentence_of_nth_paragraph(struct document Doc, int k, int m, int n) {
    return Doc.data[n-1].data[m-1].data[k-1];
}

struct sentence kth_sentence_in_mth_paragraph(struct document Doc, int k, int m) {
    return Doc.data[m-1].data[k-1];
}

struct paragraph kth_paragraph(struct document Doc, int k) {
    return Doc.data[k-1];
}


void print_word(struct word w) {
    printf("%s", w.data);
}

void print_sentence(struct sentence sen) {
    for(int i = 0; i < sen.word_count; i++) {
        print_word(sen.data[i]);
        if (i != sen.word_count - 1) {
            printf(" ");
        }
    }
}

void print_paragraph(struct paragraph para) {
    for(int i = 0; i < para.sentence_count; i++){
        print_sentence(para.data[i]);
        printf(".");
    }
}

void print_document(struct document doc) {
    for(int i = 0; i < doc.paragraph_count; i++) {
        print_paragraph(doc.data[i]);
        if (i != doc.paragraph_count - 1)
            printf("\n");
    }
}

char* get_input_text() {	
    int paragraph_count;
    scanf("%d", &paragraph_count);

    char p[MAX_PARAGRAPHS][MAX_CHARACTERS], doc[MAX_CHARACTERS];
    memset(doc, 0, sizeof(doc));
    getchar();
    for (int i = 0; i < paragraph_count; i++) {
        scanf("%[^\n]%*c", p[i]);
        strcat(doc, p[i]);
        if (i != paragraph_count - 1)
            strcat(doc, "\n");
    }

    char* returnDoc = (char*)malloc((strlen (doc)+1) * (sizeof(char)));
    strcpy(returnDoc, doc);
    return returnDoc;
}

int main() 
{
    char* text = get_input_text();
    struct document Doc = get_document(text);

    int q;
    scanf("%d", &q);

    while (q--) {
        int type;
        scanf("%d", &type);

        if (type == 3){
            int k, m, n;
            scanf("%d %d %d", &k, &m, &n);
            struct word w = kth_word_in_mth_sentence_of_nth_paragraph(Doc, k, m, n);
            print_word(w);
        }

        else if (type == 2) {
            int k, m;
            scanf("%d %d", &k, &m);
            struct sentence sen= kth_sentence_in_mth_paragraph(Doc, k, m);
            print_sentence(sen);
        }

        else{
            int k;
            scanf("%d", &k);
            struct paragraph para = kth_paragraph(Doc, k);
            print_paragraph(para);
        }
        printf("\n");
    }     
}
