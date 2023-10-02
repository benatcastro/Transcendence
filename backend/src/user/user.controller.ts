import { Body, Controller, Param } from '@nestjs/common';
import { Get, Post, Delete, Put } from '@nestjs/common';
import { UserService } from './user.service';
import { User } from '@prisma/client';

@Controller('user')
export class UserController {
    constructor(private readonly userService: UserService) {}

  @Post()
    async createUser(
    @Body() userData: { email: string; username: string; auth_type: string },
    ): Promise<User> {
        return await this.userService.create(userData);
    }

  @Get('all')
  async returnAll() {
      return await this.userService.all();
  }

  @Put('email/:id')
  async updateEmail(
    @Param('id') id: string,
    @Body('newEmail') newEmail: string,
  ) {
      return await this.userService.updateEmailById(Number(id), newEmail);
  }
}
