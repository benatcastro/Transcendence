import { Body, Injectable } from "@nestjs/common";
import { PrismaService } from "src/prisma/prisma.service";
import { Prisma, User } from "@prisma/client";
import { log } from "console";

@Injectable()
export class UserService {
  constructor(private prisma: PrismaService) {}

  async all(): Promise<User[]> {
    return this.prisma.user.findMany();
  }

  async create(data: Prisma.UserCreateInput): Promise<User> {
    return this.prisma.user.create({ data });
  }
  
  async getUsernameById(id: number): Promise<string> {
    return (await this.findById(id)).username;
  }

  async updateUser(id: number, data: Prisma.UserCreateInput) {
    return this.prisma.user.update({
      where: { id: id },
      data: data,
    });
  }
  async updateEmail(id: number, email: string) {
    return this.prisma.user.update({
      where: { id: id },
      data: { email: email },
    });
  }

  async updateUsername(id: number, username: string) {
    return this.prisma.user.update({
      where: { id: id },
      data: { username: username },
    });
  }

  async findById(id: number) {
    return this.prisma.user.findUnique({
      where: { id: id },
    });
  }

  async delete(id: number) {
    return this.prisma.user.delete({ where: { id: id }});
  }


}