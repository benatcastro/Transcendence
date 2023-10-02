import { Body, Controller, NotFoundException, Param, Query } from '@nestjs/common';
import { Get, Post, Delete, Put } from '@nestjs/common';
import { UserService } from './user.service';
import { User } from '@prisma/client';
import { log } from 'console';

@Controller('user')
export class UserController {
    constructor(private readonly userService: UserService) {}

  @Post()
    async createUser(
    @Body() userData: { email: string; username: string; auth_type: string },
    ): Promise<User> {
        return await this.userService.create(userData);
    }

  @Get()
  async returnAll() {
    log('entra');
    try {
      
    } catch (PrismaClientSer) {
      
    }
      return await this.userService.all();
  }

  @Get(':id')
  async getUserById(@Param('id') id: string) {
    log("entra");
    log(id)
      const user = await this.userService.findById(Number(id));

    log(user);
    if (!user)
      throw new NotFoundException(`User with id: ${id} does not exist.`);
    return user;
  }

  @Put('email/:id')
  async updateEmail(
    @Param('id') id: string,
    @Body('newEmail') newEmail: string,
  ) {
      return await this.userService.updateEmailById(Number(id), newEmail);
  }
}
