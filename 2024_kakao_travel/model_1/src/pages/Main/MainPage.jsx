import React from "react";
import * as S from "./MainPage.style";
import Google from "../../assets/google.png";
import { useNavigate } from "react-router-dom";

function MainPage() {
  const navigate = useNavigate();
  return (
    <S.Container>
      <S.TopBox>
        <S.TopTitle>YOUR'S JEJU</S.TopTitle>
        <S.TopLoginButton>
          <S.TopLoginButtonImg src={Google} alt="Google" />
          Continue with Google
        </S.TopLoginButton>
        <S.MainFeatBox>
          <S.MainFeatItem onClick={() => navigate("/schedule/1")}>
            make new schedule
          </S.MainFeatItem>
          <S.MainFeatItem>view my schedules</S.MainFeatItem>
        </S.MainFeatBox>
      </S.TopBox>
    </S.Container>
  );
}

export default MainPage;