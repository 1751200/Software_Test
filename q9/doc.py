md = r'''基路径：

根据公式：
$$
 V_{G} = e - n + 2
$$

+ 我们可得基路径中独立的路径个数为：19-13+2 = 8

通过基路径算法可得以下基路径：

+ 0->d->a->b1->b2->e->13->14->15->16->f->15->14->13->g->a->21

+ 0->d->a->21

+ 0->d->a->b1->a->21

+ 0->d->a->b1->b2->a->21

+ 0->d->a->b1->b2->e->13->g->a->21

+ 0->d->a->b1->b2->e->13->14->13->g->a->21

+ 0->d->a->b1->b2->e->13->14->15->14->13->g->a->21

+ 0->d->a->b1->b2->e->13->14->15->16->15->14->13->g->a->21'''


code = r'''void ModuleX (int x, int y, int Wid, char *Str) 
{
    unsigned Zcode, Bcode; 
    int i, j, k, Rec, Color; 
    long Len; 
    char Buf[72]; 
    while (*Str) 
    {
        if ((*Str & 0x80) && (*(Str+1) & 0x80))
        {
            Zcode = (*Str - 0xa1) & 0x07f;
            Bcode = (*(Str + 1) - 0xa1) & 0x07f;
            Rec = Zcode*94 + Bcode;
            Len = Rec*72L;
            fseek(fp, Len, SEEK_SET);
            fread (Buf, 1, 72, fp);
            for (i = 0; i < 24; i++) 
                for (j = 0; j < 3; j++) 
                    for (k = 0; k < 8; k++) 
                        if (Buf[i*3 + j] >> (7 - k) & 1) 
                        { 
                            Color = y + j*8 + k - 46; 
                            PutPoint(x + i, y + j*8 + k, Color); 
                        }
            x = x + 24 + Wid;
            Str += 2;
        }
    } 
    return;
}'''
