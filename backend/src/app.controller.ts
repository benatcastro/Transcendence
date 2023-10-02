import { Controller, Get, Redirect, Res } from '@nestjs/common';
import { AppService } from './app.service';
import { Url } from 'url';

@Controller()
export class AppController {
    constructor(private readonly appService: AppService) {}

  @Get()
    getHello(): string {
        return this.appService.getHello();
    }

  @Get('login')
  @Redirect(
      'https://api.intra.42.fr/oauth/authorize?client_id=u-s4t2ud-c1a95612f155f794b7ad686516054bd69ed3a7020ce03d55129777d1a053847c&redirect_uri=https://api.intra.42.fr/oauth/authorize?client_id=u-s4t2ud-c1a95612f155f794b7ad686516054bd69ed3a7020ce03d55129777d1a053847c&redirect_uri=https%3A%2F%2Fwww.example.com&response_type=code&response_type=code',
  )
  testLogin() {}
}
