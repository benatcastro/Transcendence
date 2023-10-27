import { AuthService } from './auth.service';
import { Controller, Get, Logger, Query, Redirect, Req, Res } from '@nestjs/common';
import { log } from 'console';
import { Request, Response } from 'express';
import { UserService } from 'src/user/user.service';

@Controller('auth')
export class AuthController {
    constructor(
    private readonly AuthService: AuthService,
    private readonly UserService: UserService,
    ) {}

  @Get('42/login')
    redirectToIntraApi(@Req() req: Request, @Res() res: Response) {
        res.redirect(this.AuthService.getLoginRedirectURI());
    }

  @Get('42/callback')
  async postUserAuthorization(@Query() params: any) {

      const access_token = await this.AuthService.getAccessToken(
          params.code,
          params.state,
      );

      
      const user_data = await this.AuthService.getUserFromApi(access_token);

      let user;

      user = await this.UserService.findByUsername(user_data.username);

      if (user == null) {
        user = await this.UserService.create(user);
      }
      Logger.log("Issuing JWT for user", user);
      return await this.AuthService.createJWT(user);
      
  }
}