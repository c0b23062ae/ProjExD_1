import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_img2 = pg.transform.flip(bg_img, True, False)
    koukaton3_img = pg.image.load("fig/3.png")
    koukaton3_img = pg.transform.flip(koukaton3_img, True, False)
    koukaton3_rect = koukaton3_img.get_rect()   # こうかとんRectの抽出
    koukaton3_rect.center = 300, 200            # こうかとんの中心座標を300, 200に設定
    tmr = 0
    koukaton_x = 0
    koukaton_y = 0
    while True or num == 0:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        x = tmr % 3200
        screen.blit(bg_img, [-x, 0])
        screen.blit(bg_img2, [-x+1600, 0])
        screen.blit(bg_img, [-x+3200, 0])
        screen.blit(bg_img2, [-x+4800, 0])

        key_lst = pg.key.get_pressed()              # 全キーの押下状態を取得
        if key_lst[pg.K_UP]:
            koukaton_x = 0
            koukaton_y = -1
        elif key_lst[pg.K_DOWN]:
            koukaton_x = 0
            koukaton_y = +1
        elif key_lst[pg.K_LEFT]:
            koukaton_x = -1
            koukaton_y = 0
        elif key_lst[pg.K_RIGHT]:
            koukaton_x = +2
            koukaton_y = 0
        
        koukaton3_rect.move_ip((koukaton_x-1, koukaton_y))
        koukaton_x = 0
        koukaton_y = 0


        screen.blit(koukaton3_img, koukaton3_rect)  # こうかとんをRectに従って貼り付ける
        pg.display.update()
        tmr += 1        
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()